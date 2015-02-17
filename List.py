#-*-coding:utf-8-*-

interest = ['삼성전자', 'LG전자', '네이버']

print interest[0]
print interest[1]
print interest[2]

interest.append('다음')

#print interest[0:]
print type(interest[0])
print interest[3]

interest.remove('삼성전자')

#print interest
print interest[0],interest[1],interest[2]

interest.insert(1,'하이닉스')
print interest[0],interest[1],interest[2]

#Tuple

interest2 = ('Samsung', 'LG', 'SK')
print len(interest2)
print type(interest2)

#dictionary

stock_cur = {}
print stock_cur

stock_cur['dashin'] = 30000
print stock_cur

stock_cur['daum'] = 80000
print stock_cur

print len(stock_cur)

print stock_cur['daum']

print type(stock_cur)

stock_cur['naver'] = 100000
print stock_cur

stock_cur.__delitem__('dashin')
print stock_cur

stock_list = list(stock_cur.keys())
print stock_list
