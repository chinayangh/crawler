<%
Response.AddHeader "Content-Disposition", "attachment;filename=members.xls"
Response.ContentType = "application/vnd.ms-excel"
response.write "<table width=""100%"" border=""1"" >"
response.write "<tr>"
response.write "<th width=""40%""><b>教程文章</b></th>"
response.write "<th width=""30%""><b>Username</b></th>"
response.write "<th width=""30%""><b>Password</b></th>"
response.write "</tr>"
response.write "<tr>"
response.write "<td width=""40%"">源码爱好者</td>"
response.write "<td width=""30%"">user</td>"
response.write "<td width=""30%"">mypassword</td>"
response.write "</tr>"
response.write "</table>"
%>
