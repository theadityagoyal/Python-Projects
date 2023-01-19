# import socket
# host='www.google.co.in'
#
# try:
#     addr=socket.gethostbyname(host)
#     print('IP address='+addr)
#
# except socket.gaierror:
#     print('The website does not exist')
# import urllib.parse
# url='http://www.dreamtechpress.com:80/engineering/computer-science.html'
#
# tpl=urllib.parse.urlparse(url)
#
# print(tpl)
#
# print('Scheme: ', tpl.scheme)
# print('Net location: ', tpl.netloc)
# print('Path: ',tpl.path)
# print('Port number: ', tpl.port)
# print('Total url: ', tpl.geturl())
import urllib.request
file=urllib.request.urlopen("https://www.python.org/")
print(file.read())