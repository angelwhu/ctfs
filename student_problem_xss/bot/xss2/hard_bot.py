# -*- coding: utf-8 -*-

import time
import os
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from pyvirtualdisplay import Display

display=Display(visible=0,size=(800,800))

display.start()
while True:
    try:
        r = requests.get('http://123.207.24.193:8099/xss2/read233333333_message.php')
        hash1 = r.text
        if hash1.strip()!='':
            print hash1
            driver=webdriver.Chrome()
            try:
                driver.set_page_load_timeout(10)
                driver.set_script_timeout(10)
                driver.get('http://123.207.24.193:8099/xss2/')
                #driver.get('http://123.207.24.193:8087/test_bot.php')
                driver.add_cookie({'name': 'hint',
                                   'value' : 'c2V0Y29va2llKCJmbGFnIiwgImZsYWd7eHh4eHh4eHh4eHh4eHh4eH0iLCB0aW1lKCkrMzYwMDAwMDAsICIveHNzMi9mMWFnXzFzX2gzcjNfMjMzMyIpOw==',
                                   'path' : '/',
                                 })
				#setcookie("flag", "flag{xxxxxxxxxxxxxxxx}", time()+36000000, "/xss2/f1ag_1s_h3r3_2333"); 
                driver.add_cookie({'name': 'flag',
                                   'value' : 'flag{女孩的心思你别猜.avi}',
                                   'path' : '/xss2/f1ag_1s_h3r3_2333',
                                 })
                #driver.close()
                #time.sleep(1)
                driver.get('http://123.207.24.193:8099/xss2/admin233333333_message.php?r='+hash1)
                #driver.get('http://123.207.24.193:8087/test_bot.php')
                #prevent alert to pause
                while 1:
                    try:
                        driver.switch_to_alert().accept()
                        print "alert accepted"
                    except selenium.common.exceptions.NoAlertPresentException:
                        print "no alert"
                        break
                page_source=driver.page_source
                print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time())) + ":   "+ page_source.encode('utf-8')
                time.sleep(10)
                driver.close()
                driver.quit()
                #time.sleep(1)
            except Exception as e:
                print "[ERROR] "+str(e)
                #important
                driver.close()
                driver.quit()
    except Exception as e:
        print "[ERROR] "+str(e)
    #os.system("ps aux|grep chrome|awk '{print $2}'|xargs kill -9")
    time.sleep(1)

