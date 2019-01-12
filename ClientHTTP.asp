<%
<SCRIPT ID=clientEventHandlersJS LANGUAGE=javascript>
<!--

function XMLHTTPButton_onclick() {
var DataToSend = "id=1";
var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
xmlhttp.Open("POST","http://<%=Request.ServerVariables("Server_Name")%>/Receiver.asp",false);
xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xmlhttp.send(DataToSend);
alert(xmlhttp.responseXML.xml);
}

//-->
</SCRIPT>

<INPUT type="button" value="Submit XMLHTTP" id=XMLHTTPButton name=XMLHTTPButton 
LANGUAGE=javascript onclick="return XMLHTTPButton_onclick()">


'https://support.microsoft.com/en-us/help/290591/how-to-submit-form-data-by-using-xmlhttp-or-serverxmlhttp-object

%>
