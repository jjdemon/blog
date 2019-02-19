import re

# path = "student/12"
# res = re.match(r'^student/(\d+)$',path,re.I)
# print(res.groups())

s1 = ['name=tom','password=123']
s1 = {key:value  for key,value in [value.split('=') for value in s1]}
print(s1)