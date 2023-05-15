#0418
#튜플, 딕셔너리, 집합
lst = []
lst.append(1)
print(lst)
#수정, 변경, 일부 원소 삭제 가능
#수정이 불가항목들, -> 튜플
t1=(1,2,3,4)
print(t1)
t2 = tuple()
print(t2)
t3=1,2,4,5,3,3,10,3
print(type(t3))
i=1
print(type(i))

print(t3.index(3))
print(t3.count(3))

t4=1,2,3,4,5,4,4,10,3
t5 = 100,200,300
print("t4+t5: ",t4+t5)
print("t4: ",t4)
print("t5: ",t5)

print(sorted(t4))
print("t4: ",t4)
#dictionary
#key:Value
#1001:"홍길동", 1002:"김길동"

d1={1001:"홍길동", 1002:"김길동",1003:"박길동",1004:"고길동"}
print(d1[1001])
#print(d1[key])

#d2={}
#강좌에 대한 dictionary
d2=dict()
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['년도'] = 2003
d2['수강생']=['김','이','박']
print(d2)
print(d2['수강생'])
print(len(d2))

season = {10:'1월',20:'2월',30:'3월',40:'4월',50:'5월',60:'6월',70:'7월',80:'8월',90:'9월',100:'10월',110:'11월',120:'12월'}
for i in season:print(season[i])
for i in range(1,121):
    print()

#dictionary method
print(season.keys())
print(season.values())

#for 조건:
    #실행문
print("---------------------------")
for kim in season.keys():
    print(season[i])
    print("kim: ",kim)
    print(season[kim])
print("---------------------------")
for i in season.values():
    print(i)
print("---------------------------")
print(season.items())
for item in season.items():
    print(item)
    print(item[1])
print("---------------------------")
for k,v in season.items():
    print(k)
    print(v)
print("---------------------------")
for i in season:
    print(i)
    print(season[i])
print("---------------------------")
print("month.pop(10)",season.pop(10))#key값을 주고, 해당 item을 제거
print(season.popitem()) #제일 마지막 item을 제거
print(season)

season.update({30:'March'})
print(season)
season.update({150:'15월'})

seql =['a','b','c','d']
seqt = tuple(seql)
print(seqt)
print(type(seqt))

seql2 = list(seqt)
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))