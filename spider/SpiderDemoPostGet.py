import urllib
import urllib2

# post commit
# values = {"username":"123@126.com","password":"xxxx"}
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()


# get commit
values = {}
values["username"] = "123@126.com"
values["password"] = "xxx"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
