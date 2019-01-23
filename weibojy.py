#!/usr/bin/python
# -*- coding: UTF-8 -*-
print ('Status: 200 OK')
print ('Content-type: text/html')
print ()

import cgi
import cgitb
cgitb.enable()


import requests
import re
import urllib3
urllib3.disable_warnings()
http = urllib3.PoolManager()
cookies = {"SUB":"_2A25xPaENDeRhGedM7lsXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
url = "https://weibo.cn/search/mblog/%E6%95%99%E8%82%B2?wm=ig_0001&page=2"
r = requests.get(url,cookies=cookies,verify=False)
#html=r.content
html=r.text
#start = "热门</a></div>"
start = "热门</a></div>"
#end   = "<div class=\"pa\""
end   = ">下页"
#pat = re.compile(start+'(.*?)'+end,re.S)
pat = re.compile(start+'(.*?)'+end,re.S)
result = pat.findall(html)
print("""
<head>
    <style>
        .kt {
        color: #F00;
        }
    </style>
</head>
<body>
<div align="center">
<form id="next" action="" method="post" enctype="multipart/form-data"> 
<input type="button" value="下一屏" class="btn" id="nextbtn" onclick="window.location.href = 'crawlerwbjy2.py'"/>
</form>
</div>
</body>

"""
)

print (result)
#html_doc=html.decode("gbk","ignore")
#print (html_doc)
