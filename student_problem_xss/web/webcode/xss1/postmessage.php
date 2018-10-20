<?php

/**
 * 输出二次验证结果,本文件示例只是简单的输出 Yes or No
 */
// error_reporting(0);
require_once './gt3-php-sdk-master/lib/class.geetestlib.php';
require_once './gt3-php-sdk-master/config/config.php';
session_start();
$GtSdk = new GeetestLib(CAPTCHA_ID, PRIVATE_KEY);

$code_flag=false;

$data = array(
        "user_id" => $_SESSION['user_id'], # 网站用户id
        "client_type" => "web", #web:电脑上的浏览器；h5:手机上的浏览器，包括移动应用内完全内置的web_view；native：通过原生SDK植入APP应用的方式
        "ip_address" => $_SERVER["REMOTE_ADDR"] # 请在此处传输用户请求验证时所携带的IP
    );


if ($_SESSION['gtserver'] == 1) {   //服务器正常
    $result = $GtSdk->success_validate($_POST['geetest_challenge'], $_POST['geetest_validate'], $_POST['geetest_seccode'], $data);
    if ($result) {
        $code_flag=true;
    } else{
        //echo '{"status":"fail"}';
    }
}else{  //服务器宕机,走failback模式
    if ($GtSdk->fail_validate($_POST['geetest_challenge'],$_POST['geetest_validate'],$_POST['geetest_seccode'])) {
        $code_flag=true;
    }else{
        //echo '{"status":"fail"}';
    }
}

if(!$code_flag)
{
	echo "验证码出现错误~";
	exit(-1);
}

include 'header.php';

$message = filter($_POST['message']);

//echo $message;


// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检测连接
if ($conn->connect_error) {
	die("数据库连接失败: " . $conn->connect_error);
}

// 预处理及绑定
$stmt = $conn->prepare("INSERT INTO message (content) VALUES (?)");
//var_dump($stmt);
$stmt->bind_param("s", $message);

// 设置参数并执行
$stmt->execute();


echo "留言成功,管理员会尽快阅读你的消息。";

$stmt->close();
$conn->close();

?>
