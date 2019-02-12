<%
Response.ContentType = "application/msword"
Response.AddHeader "Content-Disposition", "attachment;filename=NAME.doc"
Response.Write("欢迎来到源码爱好者!<br>" & vbnewline)
Response.Write("<h1>用ASP生成Word文档的示例</h1>")
response.write "<table width=""100%"" border=""1"" >"
response.write "<tr>"
response.write "<th width=""40%""><b>Name</b></th>"
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
