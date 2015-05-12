#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')

print "Content-type: text/html"
print

try:
	print "Full Name: " + val1 +' '+ val2
except TypeError:
	print ""

print "<br/><br/>"
print "Enter Birthday: "
print """<form method="post" action="nameform.py">
		 <textarea name="birthday" cols="20" rows="5">
		 </textarea><br/>"""

print "Enter Hobbies: "
print """<br/> <form method="post" action="nameform.py">
		 <textarea name="hobbies" cols="20" rows="5">
		 </textarea><br/> <input type="submit" value="Submit">
		 </form>"""

