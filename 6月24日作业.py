import re

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

a = re.match('(\w+)\s+([0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+)\s+[A-Z]+\s+\w+/\d/\d+',str1.strip())
abc = re.match('(\w+)\s+([0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+)\s+([A-Z]+)\s+(\w+/\d/\d+)',str1.strip()).groups()
# print(a)
print(abc)

print(f'{"VLAN ID":<15}: {abc[0]:<10}')
print(f'{"MAC":<15}: {abc[1]:<10}')
print(f'{"Type":<15}: {abc[2]:<10}')
print(f'{"Interface":<15}: {abc[3]:<10}')
