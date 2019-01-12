<%@ Language=vbScript%>
<%
DataToSend = "id=1"
dim xmlhttp 
set xmlhttp = server.Createobject("MSXML2.ServerXMLHTTP")
xmlhttp.Open "POST","http://localhost/Receiver.asp",false
xmlhttp.setRequestHeader "Content-Type", "application/x-www-form-urlencoded"
xmlhttp.send DataToSend
Response.ContentType = "text/xml"
Response.Write xmlhttp.responsexml.xml
        Set xmlhttp = nothing
%>

'https://support.microsoft.com/en-us/help/290591/how-to-submit-form-data-by-using-xmlhttp-or-serverxmlhttp-object
