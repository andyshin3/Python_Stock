#coding:utf-8

import matplotlib.pyplot as plt
x = range(100)
y = [i*i for i in x]
plt.plot(x,y)
plt.show()