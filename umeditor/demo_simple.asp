<%
	Session.CodePage = 65001

	' Change this to your own SMTP server
	strHost = "localhost"
	
	if Request("Send") <> "" Then
		
		Set objMail = Server.CreateObject("Persits.MailSender")

		objMail.Host = strHost

		objMail.From = "hai@WIN-8R5LFDSRQV9.com"	' From address
		'objMail.Username = ""
		'objMail.Password = ""
		objMail.FromName = "舆情提醒摘要"		' optional

		strToAddress = Trim(Request("txtTo"))

		' To prevent header injection attack
		strToAddress = Replace( strToAddress, " ", "" )
		strToAddress = Replace( strToAddress, chr(13), "" )
		strToAddress = Replace( strToAddress, chr(10), "" )

		' To address, 2nd argument omitted.
		objMail.AddAddress strToAddress
		
		' Message subject
		objMail.Subject = objMail.EncodeHeader( Request("txtSubject"), "UTF-8" )

		' Enable Unicode
		objMail.ContentTransferEncoding = "Quoted-Printable"
		objMail.CharSet = "UTF-8"
		objMail.IsHTML = True
		
		' Message body
		'objMail.Body = Request("txtBody")
		objMail.Body = Request.Form("myEditor")

		On Error Resume Next
		objMail.Send ' Send message

		If Err = 0 then		
			txtMsg = "<font color=green>Success! Message sent to " & strToAddress + ".</font>"
		Else		
			txtMsg = "<font color=red>Error occurred: " + err.Description + "</font>"
		End If
	
	End If
%>

<HTML >
<HEAD>

<META HTTP-EQUIV="Content-Type" content="text/html; charset=utf-8">

<TITLE>AspEmail</TITLE>
<link href="themes/default/css/umeditor.css" type="text/css" rel="stylesheet">
    <script type="text/javascript" src="third-party/jquery.min.js"></script>
    <script type="text/javascript" charset="utf-8" src="umeditor.config.js"></script>
    <script type="text/javascript" charset="utf-8" src="umeditor.min.js?20190215"></script>
    <script type="text/javascript" src="lang/zh-cn/zh-cn.js"></script>
</HEAD>
<BODY style="font-family: arial narrow; font-size: 10pt">

<h2>AspEmail Live Demo: Unicode-enabled Message Sending</h2>

<P> 


<FORM METHOD="POST" ACTION="demo_simple.asp">

<TABLE CELLSPACING=2 CELLPADDING=2 BGCOLOR="#E0E0E0" style="border: 1pt black solid; border-collapse: collapse">
	<TR>
		<TD>To:</TD>
		<TD><INPUT TYPE="TEXT" size="40" NAME="txtTo" VALUE="<% = Server.HtmlEncode(Request("txtTo")) %>"></TD>
	</TR>
	<TR>
		<TD>Subject:</TD>
		<TD><INPUT TYPE="TEXT" size="40" NAME="txtSubject" VALUE="<% = Server.HtmlEncode(Request("txtSubject")) %>"></TD>
	</TR>
	<TR>
		<TD valign="top">Body:</TD>
		<TD style="display:none;"><TEXTAREA NAME="txtBody" ><% = Server.HtmlEncode(Request("txtBody")) %></TEXTAREA></TD>


<script type="text/plain" id="myEditor" name="myEditor" style="width:500px;height:240px;">
    
</script>

<script type="text/javascript">
    //实例化编辑器
    var um = UM.getEditor('myEditor');
 

</script>

	</TR>
	<TR>
		<TD COLSPAN=2><INPUT TYPE="SUBMIT" NAME="Send" VALUE="Send Message"></TD>
	</TR>

</TABLE>

<P>

<% = txtMsg %>

</FORM>

</BODY>
</HTML>
