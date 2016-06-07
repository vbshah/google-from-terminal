import sys
from subprocess import call
import requests as re
from bs4 import BeautifulSoup as bs
import urllib
import select
import webbrowser

def remove(s):
	s=s[7:]
	for i in range(len(s)):
		if s[i:i+3]=='&sa':
			break
	return s[0:i]

ls=sys.argv
browser="firefox"
q='http://www.google.co.in/search?q='+'+'.join(ls[1:])
print 'q',q
links=[]
while len(links)==0:
#        q='http://www.google.com/search?q=i+dont+know'
        r=re.get(q)
        soup=bs(r.text,"lxml")
        links=[]
        for link in soup.findAll('h3',{'class','r'}):
                for l2 in link('a'):
                        s=str(l2.get('href'))
                        s=urllib.unquote(s.encode('utf8'))
                        if s.count('http') or s.count('https'):
                                print remove(s),':--:-=:',''.join(l2.findAll(text=True))
#                                call(['nohup',browser,remove(s)])	
                                webbrowser.open(remove(s))
                                links.append(s)
                break
        print 'we got',len(links)
i, o, e = select.select( [sys.stdin], [], [], 5 )
if i:
#	call([browser,remove(links[int(sys.stdin.readline().strip())])])
        webbrowser.open_new(remove(links[int(sys.stdin.readline().strip())]))
else:
	print 'you cannot type anything'
	call(['exit'])
