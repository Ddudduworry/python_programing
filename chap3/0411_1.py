#0411
#리스트, 튜플, 딕셔너리, 집합
#김, 이, 박, 최,
#리스트['김','이','박','최']
#튜플('김','이','박','최')
#딕셔너리 -> 사전 {key:value,k1:v1,k2:v2,....}

#address={'홍길동':'서울','김길동':'부천','jamse':'미국'}
#print(address['홍길동'])

#list
#숫자, int, float, string  다 가능함
lst = [10,20,30,40,50]
str_list=['하','호']
print(type(lst))
print(lst[0]," ",str_list[1]," ", lst[len(lst)-1])

#빈리스트 생성 -> 하나씩 원소를 추가
list1=[]
#list2=list()
print(list1)
list1.append("python")
list1.append("java")
list1.append("c++")
print(list1)
print(list1[0])
print("===for 1=====")
for i in range(len(list1)):print(list[i])
print("===for 2=====")
for i in list1:print(i)

print(list1)
print("count : ",list1.count("python"))
print("index : ", list1.index("python"))

#list 수정
list1[0]="AI"
list1[2]="Iot"
print(list1)
print("------------------")
#수정 불가-> append, insert, 값 변경.x
list2 = list1[0:3:1]
print(list2)
list2 = list1[1:5:1]
print(list2)
list2 = list1[1:len(list1):2]
print(list2)
list2 = list1[2:6:3]
print(list2)
list2 = list1[::-1]
print(list2)

#list insert
food = []
food.append("짜장면")
food.append("샌드위치")
food.append("로제엽떡")
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"제육")
print(food)

food.remove("제육")
print(food)

#print("food.pop: ",food.pop())
#print("food.pop: ",food.pop())
print(food)
#print("food.pop: ",food.pop())
print(food)
print("---------------------------")
#extend
print(food)
dessert=["커피","케잌","와플"]

food_list = food + dessert
print(food_list)

#food.extend(dessert)
#print(food)

#food.clear()
#del food
#print(food)

food.reverse()
print(food)

l1 =["banana","apple","orange","mango"]

a="1"
print(type(a))
print(int(a) + 5)#잠시만 a가 int 형이 된것
print("----------------")
food.sort()
print(food)


