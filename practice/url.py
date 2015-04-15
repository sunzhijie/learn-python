import urllib
baidu = urllib.urlopen('http://baidu.com')
def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

url = 'http://www.sina.com.cn'
local = 'sina.html'
urllib.urlretrieve(url, local, cbk)
baidu.close()
