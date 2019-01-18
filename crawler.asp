<%@LANGUAGE="VBSCRIPT" CODEPAGE="936"%>
<!DOCTYPE HTML ">
<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=gbk">
<title></title>
</head>
<%
Set objXML = Server.CreateObject("MSXML2.ServerXMLHTTP")
objXML.open "GET","http://news.baidu.com/ns?word=%E6%95%99%E8%82%B2",false
objXML.send()
response.write(objXML.responseText)

%>
<body>
</body>
</html>