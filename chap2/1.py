#1.py
'''이것은 여러줄로
이루어진 주석입니다'''


print("hello world!!")
print("파이썬" + "만세")
print("파이썬" + "만" +"세"+"!!")
print("파이썬!!!" *3)

print("hello 'world'!!")
print('hello "world"!!')
print(type("hello"))
print(type(1.1))

print(1,2,-5,3.14,2.71828)
print('hi','python')
print('23000원','5000원 ?개', '1000원 ?개')
print('5000원',23000//5000,'개')
print('1000원',(23000%5000)//1000,'개')
print(eval('3+15/2'))
print(eval('4*3%5'))

print(eval('1+62-3*52'))
print(256*553-152)

print(eval('1632665%445')*eval('1632665/445'))

result = 78000%50000
print('50000원',78000//50000,'개')
print('10000원',result//10000,'개')
c=result%10000
print('5000원',c//5000,'개')
d=c%5000
print('1000원',d//1000,'개')
