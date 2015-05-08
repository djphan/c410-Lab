# CMPUT410_Lab1
This is the lab 1 assignment for CMPUT 410. It is a review of Python, Github, Virtualenv, and Curl/

# Git Commands
* git init
* git add .
* git commit
* git remote add origin "<URL>"
* git remote -v 
* git pull remote origin
* git push --set-upstream origin master

# Virtualenv Commands
* virtualenv virt_env/virt1 --no-site-packages
* source virt_env/virt1
* deactivate

# CURL Commands
* curl -X PUT -H'Content-Type: application/json' -d'{"firstName":"Kris", "lastName":"Jordan"}' echo.httpkit.com
* curl --request POST 'http://www.somedomain.com/' 
* curl --request DELETE 'http://www.somedomain.com/' 
* curl --request PUT 'http://www.somedomain.com/'
