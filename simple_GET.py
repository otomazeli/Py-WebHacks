import urllib2

url = "http://www.google.com"
body = urllib2.urlopen("http://www.google.com")

print body.read()
