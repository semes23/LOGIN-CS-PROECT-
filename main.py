#menu
import login
import register
import mysql.connector as ms
mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')

print('connected!')
mycursor = mycon.cursor()
mycursor.execute('select * from login_info;')
login_data = mycursor.fetchall()
mycursor.execute("select * from reg;")
reg_data = mycursor.fetchall()
print('WELCOME TO SKYTOUCH!!')
ch=input('> ')
if ch=='1' :
    login.verify()
elif ch=='2':
    register.fun()


print('hi')