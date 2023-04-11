#리스트 컴프리헨션 목적:코드를 간단히하고싶은 마음
#0-10까지 있는 list를 만들자
#1)
l3=[0,1,2,3,4,5,6,7,8,9,10]

#2)
l3=[]
for i in range(11) :
    l3.append(i)
print(l3)

#3)리스트 컴프리렌션
#리스트 변수명 = [i for i in range() ]
l3 = [i for i in range(11)]
print(l3)

#10
#0~10까지의 숫자의 제곱을 원소로 가지는 리스트를 작성
#i**2
#[1,2,4,9,16,...,64,81,100]

l4 = [i**2 for i in range(11)]
print(l4)

l5 = [i*3 for i in range(11)]
print(l5)

l6=["hello" for i in range(11)]
print(l6)

#0-10까지의 숫자의 제곱을 리스트로 만들어라
#짝수의 제곱만 넣어라
l7=[]
for i in range(11):
    if(i%2==0):
        l7.append(i**2)
print(l7)

l8 =[i**2 for i in range(11) if i%2 ==0]
print(l8)

#shallow copy
food = []
food.append("짜장면")
food.append("샌드위치")
food.append("로제엽떡")
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"제육")
print(food)

wishlist = food
print("food:     ",food)
wishlist = food
print("wishlist:    ",wishlist)

food.pop()
print("after food.pop()")
print("food:    ",food)
print("wishlist: ",wishlist)

print(food is wishlist)
print("---------")
#deep copy
food2 = food[:]
print("deep copy ")
print("food:   ",food)
print("food2:   ",food2)
print(food is food2)

food2.append("김밥")
print("deep copy ")
print("food:   ",food)
print("food2:   ",food2)
print(food is food2)