#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('birthday')
val2 = form.getvalue('hobbies')

 
print "Content-type: text/html"
print 
print "Enter First Name Here: "
print """<form method="post" action="birthform.py">
		 <textarea name="name" cols="20" rows="5">
		 </textarea><br/>"""


print "Enter Family Name Here: "
print """<br/><br/><form method="post" action="birthform.py">
		 <textarea name="family" cols="20" rows="5">
		 </textarea><br/> <input type="submit" value="Submit">
		 </form>"""

print "<br/>"

try:
	print "Birthday: " + val1  
	print "<br\>"
	print "Hobbies: " + val2
except TypeError:
	print ""
 

 

