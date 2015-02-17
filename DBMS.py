#coding:utf-8

import sqlite3

#db와 연결된 객체 생성
con = sqlite3.connect('kospi.db')
print type(con)

#객체의 커서 생성
cursor = con.cursor()

#커서내에 테이블 생성
#cursor.execute('CREATE TABLE kospi(Name text, ClosingPrice int)')

#행에 데이터 삽입
#cursor.execute("INSERT INTO kospi VALUES(\"LG전자\", 74500)")
#cursor.execute("INSERT INTO kospi VALUES(\"네이버\", 774000)")
#cursor.execute("INSERT INTO kospi VALUES(\"다음\", 169100)")

#DB에 반영을 위해서 커밋
con.commit()

#DB와 연결 해제
con.close()

#DB에 다시 접속

con = sqlite3.connect('kospi.db')
cursor = con.cursor()

#DB에서 데이터 읽기 (중복제거)
cursor.execute("SELECT DISTINCT * FROM kospi")
#for row in cursor:
#    print row

#한 행씩 출력
print cursor.fetchone()

mydata = cursor.fetchall()
print mydata
print mydata[0][0]
print mydata[0][1]
print mydata[1][0]
print mydata[1][1]