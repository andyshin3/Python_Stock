#coding:utf-8

mystring = 'Hello World'

print mystring[0:-1]

print type('Hello')

print mystring.split(' ') [0]

print 'daum' +' ' +'kakao'

#Problem 1

s = 'Daum KaKao'

daum = s.split(' ')[0]
kakao = s.split(' ')[1]

s2 = kakao + ' ' + daum

print s2

#Problem 2
a = 'hello world'
b = a.split(' ') [1]
print ('hi' + b)

#Problem 3
x = 'abcdef'
print x[1:] + x[0]
