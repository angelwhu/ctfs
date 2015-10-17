import sys 
import crypt, getpass, pwd

from datetime import date
from dateutil.rrule import rrule, DAILY


reslut = "$6$F84utBXh$g2dDb6QXacuId.5NDwrvyPxIJGxiU8gyhTywRP5jksb6e/CgeG94/THLJhgZ4oB8hPowrLPdmVWFIZTBZdT6S/"
a = date(1940,  1, 1)
b = date(2015, 10,30)

for dt in rrule(DAILY, dtstart=a, until=b):
    passdate = dt.strftime("%Y%m%d")
    # root:$6$F84utBXh$g2dDb6QXacuId.5NDwrvyPxIJGxiU8gyhTywRP5jksb6e/CgeG94/THLJhgZ4oB8hPowrLPdmVWFIZTBZdT6S/:16680:0:99999:7::
    passwd  = "joker" + passdate
    print passwd 
    crypted = crypt.crypt(passwd, '$6$F84utBXh$')
    print crypted
    if crypted == "$6$F84utBXh$g2dDb6QXacuId.5NDwrvyPxIJGxiU8gyhTywRP5jksb6e/CgeG94/THLJhgZ4oB8hPowrLPdmVWFIZTBZdT6S/" :
        print "success"
        exit()

print reslut == "$6$F84utBXh$g2dDb6QXacuId.5NDwrvyPxIJGxiU8gyhTywRP5jksb6e/CgeG94/THLJhgZ4oB8hPowrLPdmVWFIZTBZdT6S/"
