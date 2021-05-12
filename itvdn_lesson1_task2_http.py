from urllib import request

response = request.urlopen('https://www.google.com/')


print('Response status: ', response.status)
print('Response code: ', response.getcode())
print('Response message: ', response.msg)
print('Response reason: ', response.reason)

print(response.headers)

print(response.getheaders())

print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))