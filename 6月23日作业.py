
a1 = 'QYTANG'
a2 = '\'day'
a3 = ' 2014-9-28'

b = a1+a2+a3
print(b)

print('='*20)

word = "scallywag"
sub_work = word[2:6]
print(sub_work)

print('='*20)

c = 'Thanks'
newc = c[1:]+'-'+c[0]+'y'
print(newc)

print('='*20)

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'wangxiao'
COURSE_FEES_SEC = 123456.56789
COURSE_FEES_Python = 9876.54321

# line1 ='Department1 name:%-10s Manager:%-10s COURSE FESS:%-10.2f The End!'%(department1,depart1_m,COURSE_FEES_SEC)
# line2 ='Department2 name:%-10s Manager:%-10s COURSE FESS:%-10.2f The End!'%(department2,depart2_m,COURSE_FEES_Python)

# line1 ='Department1 name:{0:<10} Manager:{1:<10} COURSE FESS:{2:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
# line2 ='Department2 name:{0:<10} Manager:{1:<10} COURSE FESS:{2:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)

line1 =f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FESS:{COURSE_FEES_SEC:<10.2f} The End!'
line2 =f'Department2 name:{department2:<10} Manager:{depart2_m:<10} COURSE FESS:{COURSE_FEES_Python:<10.2f} The End!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

