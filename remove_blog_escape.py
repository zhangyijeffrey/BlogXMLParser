import string 

file_in = open("blog.xml", 'r')
f = file_in.read()

f = string.replace(f, "&nbsp;", " ")
f = string.replace(f, "&lt;", "<")
f = string.replace(f, "&gt;", ">")
f = string.replace(f, "&amp;", "&")

file_in.close()

file_out = open("blog_remove_escape.xml", 'w')
file_out.write(f)
