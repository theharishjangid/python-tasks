x = int(input('enter no of ele'))
s = set()
for i in range(x):
	a = int(input('enter ele'))
	s.add(a)
print(s)

s2 = {1, 2, 3, 4, 5}

s3 = s | s2
print('union',s3)

s4 = s & s2
print('intersection',s4)

s5 = s - s2
print('diff',s5)


	

