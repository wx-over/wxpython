import re
'''
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

a = re.match('(\w+)\s+([0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+)\s+[A-Z]+\s+\w+/\d/\d+',str1.strip())
abc = re.match('(\w+)\s+([0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+)\s+([A-Z]+)\s+(\w+/\d/\d+)',str1.strip()).groups()
# print(a)
print(abc)

print(f'{"VLAN ID":<15}: {abc[0]:<10}')
print(f'{"MAC":<15}: {abc[1]:<10}')
print(f'{"Type":<15}: {abc[2]:<10}')
print(f'{"Interface":<15}: {abc[3]:<10}')
'''
str2 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

c = re.match('([A-Z]+)\s+([a-z]+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+([a-z]+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),\s+([a-z]+)\s+(\d{1,2}:\d{1,2}:\d{1,2}),\s+([a-z]+)\s+(\d+),\s+([a-z]+)\s+(\w+)',str2.strip())
conn = re.match('([A-Z]+)\s+([a-z]+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+([a-z]+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),\s+([a-z]+)\s+(\d{1,2}:\d{1,2}:\d{1,2}),\s+([a-z]+)\s+(\d+),\s+([a-z]+)\s+(\w+)',str2.strip()).groups()

t = conn[6]
time = t[0]+' 小时 '+t[2:4]+'分钟 '+t[-2:]+'秒'

# print(c)
# print(conn)
print(f'{"protocol":<15}: {conn[0]:<10}')
print(f'{conn[1]:<15}: {conn[2]:<10}')
print(f'{conn[3]:<15}: {conn[4]:<10}')
print(f'{conn[5]:<15}: {time:<10}')
print(f'{conn[7]:<15}: {conn[8]:<10}')
print(f'{conn[9]:<15}: {conn[10]:<10}')





