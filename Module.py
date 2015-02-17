#coding:utf-8

def repeat(number):
    i = 0
    while i < number:
        print ('pizza')
        i += 1

print repeat(4)

##Return

def cal_upper(start_cost):
    start_cost *= 1.15
    return start_cost

def cal_lower(start_cost):
    start_cost *= 0.85
    return start_cost


def get_u_l(start_cost):
    u=start_cost*1.15
    l=start_cost*0.85
    return(u,l)

print cal_upper(10000)
print cal_lower(10000)
print get_u_l(10000)


# import
import os

print dir(os)
print os.getcwd()
print os.listdir(os.getcwd())
print len(os.listdir(os.getcwd()))

for x in os.listdir(os.getcwd()):
    if x.endswith('py'):
        print(x)