import urllib.request as request
import re

crawl = []
re1 = re.compile('<span.*span>')
for i in range(1,26):
    url = request.urlopen("http://ec2-54-180-137-70.ap-northeast-2.compute.amazonaws.com:8090/review/main/?pageNum="+str(i))
    urllist = list(url)
    for i in urllist:
        i = i.decode("utf-8")
        if(re1.search(i)):
            crawl.append(i)
re2 = re.compile('[>].*[|]')
re3 = re.compile('[|].*[<][b][r][>][<][/][s]')
tmp = []
for i in crawl:
    tmp.append(i[re2.search(i).start()+1:re3.search(i).end()-7])
id_time = dict() ; j=0
re4 = re.compile('[|]')
for i in tmp:
    a = re4.search(i).start()
    id_time[i[:a-2]] = i[a+3:]
print (id_time['admin'])