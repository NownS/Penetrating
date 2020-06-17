import re

f = open("netstat.txt","r", encoding = "UTF-8", newline='')
netstat = []
while True:
    line = f.readline()
    if not line: break
    netstat.append(line)
f.close()
crawl = []
iplist = []
p = re.compile(':80\s*ESTABLISHED')
for i in netstat:
    if(p.search(i)):
        crawl.append(i)
ip = re.compile('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
for i in crawl:
    iplist.append(ip.findall(i)[1])
print ("80 PORT ESTABLISHED IP")
for i in iplist:
    print(i)