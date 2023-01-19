import urllib.request
file=urllib.request.urlopen("https://www.python.org/")
print(file.read())
