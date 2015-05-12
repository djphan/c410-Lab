#!/usr/bin/env python
 
print "Content-type: text/html"
print 
print """<form method="post" action="testform.py">
	<textarea name="comments" cols="40" rows="5">
	Enter comments here...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
