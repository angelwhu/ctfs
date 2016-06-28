import hashlib   

def md5(src):
    m2 = hashlib.md5()
    m2.update(src)   
    return m2.hexdigest()   

def go():
    chars = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|~"
    for i in chars:
        for j in chars:
            for k in chars:
                for l in chars:
                    tmp = i + j + k +l
                    md5_value = md5(tmp)
                    if md5_value[3:9] == "81a427":
                        print tmp
                        print md5_value
def test():
    tmp = md5("123")
    print tmp
    print tmp[3:9]

if __name__ == "__main__":
    go()
    #test()
