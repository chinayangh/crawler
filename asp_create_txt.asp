<%
set objFso = server.createobject("scripting.filesystemobject")
set objFile = objFso.CreateTextFile("sample.txt", false)
objFile.write "这是一个生成txt文本的演示文档"
objFile.close
set objFile = nothing
objFso = nothing
%>
