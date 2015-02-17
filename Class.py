#coding:utf-8

class BusinessCard:
    def setinfo(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def printinfo(self):
        print ('----------------')
        print ('Name : %s' % self.name)
        print ('E-mail : %s' % self.email)
        print ('Address : %s' % self.addr)
        print ('----------------')


print type(BusinessCard)

member1 = BusinessCard()
member1.setinfo('Andy', 'andyshin3@gmail.com', 'Paju')
print member1.name
print member1.email
print member1.addr
print member1.printinfo()

class BusinessCard2:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def printinfo(self):
        print ('----------------')
        print ('Name : %s' % self.name)
        print ('E-mail : %s' % self.email)
        print ('Address : %s' % self.addr)
        print ('----------------')


print type(BusinessCard2)

member1 = BusinessCard2('Andy', 'andyshin3@gmail.com', 'Paju')

print member1.name
print member1.email
print member1.addr
print member1.printinfo()

##Self
class Foo:
    def func1():
        print('func1')
    def func2(self):
        print(id(self))
        print('func2')

#Class + Method (Obj)
f3 = Foo()
print Foo.func2(f3)

#Obj + Method
f = Foo()
print f.func2()