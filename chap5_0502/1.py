#0502
#함수
#input을 주면 output이 나오는 것
'''
input - 숫자 - num1
output = 숫자 - ouput_num
이런 기능을 하는 function - multi
'''

#함수 정의
def multi(num1) :
    output_num = num1 * 3
    return output_num

#정의한 함수를 호출한다.
x=10
print(multi(x))
print(multi(15))

print("----------------------------")
#안녕 이름, 안녕 이름 출력 함수
def hello(name1="홍",name2="길") :
    print('안녕 {}, 안녕 {}'.format(name1,name2))
    
    ''' 교수님 답안
    print("안녕 ,",name1)
    print("안녕 ," name2)
    '''

hello('유정','정원')
hello() #파라메터에 기본값을 줌으로써 오류를 막는다.

print("----------------------------")
#두개의 합을 함수내에서 출력하는 함수
def twosum(num1, num2) :
    ouput = num1 + num2
    print(ouput)

twosum(8,8)
print("----------------------------")
def twosum2(num1, num2) :
    return num1+num2

result = twosum2(8,8)
print(result)
print(twosum2(100,2000))

print("----------------------------")

#지역 변수, 전역 변수
num = 100 #전역 변수 global variable
print("**** num : ", num)

def addone() :
    global num
    num = num+1
    #print(num + 1)
    #print("addone() num : ", num)

addone()
print(num)

#인자의 갯수가 여러개인 경우 ex)print()
def hello2(*names) :
    #안녕 찍기
    for i in names :
        print("hello ", i)

hello2('김유정','김정원','코끼리','피곤해','집갈래')

#합을 구하는 function
def mysum2(*numbers) :
    sum = 0
    for i in numbers :
        sum += i
    print(sum)
    return sum

mysum2(1,8,5,6,9,4,5,2,2,55,5)
lst1 = [1,2,1,2,1,2,4,5,67,4]
mysum2(*lst1)
print("----------------------------")
#dictionary = {key1:value1, key2:value2}
coffee = {"아메":2000, "라떼":3000, "티":2500}

def printmenu(**keyvalue) :
    for key in keyvalue :
        print(key, keyvalue[key])

printmenu(**coffee)
printmenu(아메=2000, 코끼리=3443, 아줌마=2943)
print("----------------------------")
def func1(*num, **menu) :
    #nume들의 합
    #menu를 출력하라.
    for key in menu :
        print(key, menu[key])
    sum = 0
    for i in num :
        sum +=i
    print("숫자합: ",sum)

func1(*lst1,**coffee)
func1(4,4,5,5,1,5,5,1,2,4,**coffee)

#lambda function
#function를 만드는데, 이름짓기가 귀찮다. 실행문이 하나밖에 없다.

def addone(x) :
    return x+1

print(addone(100))

#lambda parameter_name : parameter로 실행하는 문
print((lambda x: x+1)(100))

def mysum2(num1, num2) :
    return num1 + num2

print(mysum2(100,1000))
print((lambda num1, num2 : num1 + num2)(100,1000))

#map, filter
lst1 = [1,2,3,4,5,6,7]
print(list(map(lambda x : x+1,lst1)))
print("----------------------------")
#lambda num1, num2 : num1+num2
lst1 = [1,2,3,4,5,6,7]
lst2 = [1,2,3,4,5,6,7]
plst = list(map(lambda x,y:x**y,lst1,lst2))
print(plst)