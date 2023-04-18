#zip
#list, tuple 가 여러개 -> 하나의 튜플의 조합으로 된 리스트로.
l1 = ['1조','2조','3조']
YA = ['홍','김','이']
YB = ['최','한','James']

z=zip(l1, YA, YB)
print(type(z))
print(z)
print(list(z))
print(tuple(z))

print(tuple(zip(l1,YA,YB)))

l10 = ['한식', '양식', '중식','분식']
l11 = ['전주식당','닥터로빈','취영루','토마토']
l12 = ['제육','파스타','짬뽕','김밥']

print(list(zip(l10,l11,l12)))
for i in range(4):
    print(l10[i],l11[i],l12[i])

l100 = list(zip('ABCD',l10,l11,l12))
for i in l100:
    print(i[0],i[1],i[2],i[3])

print(list(zip(l10,l11)))
print(dict(zip(l10,l11)))
print(dict(zip(l10,zip(l11,l12))))

print(list(enumerate(l11)))
print(dict(enumerate(l11)))

l21 = ['파이썬','C++','AI','JAVA','SPRING']
l22 = [101,102,103,104,105]
#dictionary로 만든다
#for문
#quit이 들어올때까지 계속 받는다.
#input() => 강의명 입력
#강의실을 알려줌
l23 = (dict(zip(l21,l22)))
print(l23)

lecture = ['파이썬','C++','AI','JAVA','SPRING']
space = [101,102,103,104,105]
d = dict(zip(lecture,space))
while True:
    c=input("강의명을 쓰세요")
    if c== "quit":
       print("종료하겠음")
       break
    else :
        print(d[c])