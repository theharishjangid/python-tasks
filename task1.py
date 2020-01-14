x=int(input('enter no of ele'))
l=list()
for i in range(x):
    a=int(input('enter ele'))
    l.append(a)

print(l)

l.sort()
print('sorted', l)

l.reverse()
print('reversed', l)
print('total', sum(l))
print('length', len(l))




	

