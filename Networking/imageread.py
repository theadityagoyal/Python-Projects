import urllib.request

url="http://personal.psu.edu/xqz5228/jpg.jpg"

download=urllib.request.urlretrieve(url, "myimage.jpg")
