import urllib.request

# 先指定的url地址发起请求，并返回服务器相应的数据（文件对象）
response = urllib.request.urlopen('http://www.baidu.com')
data = response.read()
print(data)
print(type(data))

with open(r'C:\Users\Administrator\Desktop\note\python_tuling\TUling笔记\爬虫\files\1.html','wb') as f:
    f.write(data)
