import urllib.parse
url='http://www.dreamtechpress.com:80/engineering/computer-science.html'

tpl=urlparse(url)

print(tpl)

print('Scheme: ', tpl.scheme)
print('Net location: ', tpl.netloc)
print('Path: ',tpl.path)
print('Port number: ', tpl.port)
print('Total url: ', tpl.geturl())
