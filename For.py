#coding:utf-8

#For
s = ['dashin', 'daum', 'naver']

for i in range(len(s)):
    print (s[i])


#While

wikidocs = 10000
days = 1

while days < 6:
    wikidocs *= 1.15
    days += 1
    print wikidocs


#IF

rain = 1
sum = 0
today = 1
if today == rain:
    print ('우산을 챙기자')
else:
    print ('우산을 챙기지 않는다.')
