#coding:utf-8

x = 300

print id(x)

#case 1

x = 100
y = 100

print id(x)
print id(y)

#case 2

x = 400
y = x

print id(x)
print id(y)

#Problem 1

daum = 89000
naver = 751000

someone = daum * 100 + naver * 20

print (someone)

#Problem 2

daum *= 0.95
naver *= 0.9

someone = daum * 100 + naver * 20

print daum
print naver
print (someone)

#Problem 3
F = 50

C = (F-32)/1.8

print C

#Problem 4

for n in range(10):
    print 'pizza'

#Problem 5
naver = 1000000

for n in range(5):
    naver *= 0.85

print naver

