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