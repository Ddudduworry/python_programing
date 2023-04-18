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

season = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
for i in season:print(season[i])
for i in range(1,13):
    print(season[i])

#dictionary method
print(season.keys())
print(season.values())