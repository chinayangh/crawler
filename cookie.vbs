Dim http 
'set http =  WScript.CreateObject("MSXML2.serverXMLHTTP")
set http =  WScript.CreateObject("MSXML2.serverXMLHTTP")
http.open "POST", "https://weibo.cn/search/mblog/%E6%95%99%E8%82%B2?wm=ig_0001&page=3", false
http.setRequestHeader "Cookie", "SUB=_2A25xPaENDeRhGedM7lsYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
http.setRequestHeader "Cookie", "SUB=_2A25xPaENDeRhGedM7lsYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
http.send
WScript.Echo http.status
WScript.Echo http.responseText
