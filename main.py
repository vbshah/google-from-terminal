import sys
from subprocess import call
import requests as re
from bs4 import BeautifulSoup as bs
import urllib
import select
import webbrowser

def remove(s):
<<<<<<< HEAD
        s=s[7:]
        for i in range(len(s)):
                if s[i:i+3]=='&sa':
                        break
        return s[0:i]
=======
	s=s[7:]
	for i in range(len(s)):
		if s[i:i+3]=='&sa':
			break
	return s[0:i]
>>>>>>> 8f1f4b4f651fa41fb4ca93fe0a16a457ac6d976c

ls=sys.argv
browser="firefox"
q='http://www.google.co.in/search?q='+'+'.join(ls[1:])
print 'q',q
links=[]
while len(links)==0:
        r=re.get(q)
        soup=bs(r.text,"lxml")
        links=[]
        for link in soup.findAll('h3',{'class','r'}):
                for l2 in link('a'):
                        s=str(l2.get('href'))
                        s=urllib.unquote(s.encode('utf8'))
                        if s.count('http') or s.count('https'):
                                print remove(s),':--:-=:',''.join(l2.findAll(text=True))
<<<<<<< HEAD
#                                call(['nohup',browser,remove(s)])      
#                                webbrowser.open_new(remove(s))
=======
                                webbrowser.open(remove(s))
>>>>>>> 8f1f4b4f651fa41fb4ca93fe0a16a457ac6d976c
                                links.append(s)
                                webbrowser.get('firefox').open(remove(s))
                break
        print 'we got',len(links)
        break
"""
i, o, e = select.select( [sys.stdin], [], [], 5 )

if i:
<<<<<<< HEAD
#       call([browser,remove(links[int(sys.stdin.readline().strip())])])
        webbrowser.open_new(remove(links[int(sys.stdin.readline().strip())]))
else:
        print 'you cannot type anything'
        #call(['exit'])
"""
=======
        webbrowser.open_new(remove(links[int(sys.stdin.readline().strip())]))
else:
	print 'you cannot type anything'
	call(['exit'])
>>>>>>> 8f1f4b4f651fa41fb4ca93fe0a16a457ac6d976c
