#binary converter
#Composer: Sebastiani Aguirre


import sys
from math import log

array=[]
n =  int(sys.argv[1])
pows = int(log(n,2))
x=range(pows+1)
x.reverse()
for i in x:
	if pow(2,i) > n:
		array.append(str(0))
	else:
		n= n - pow(2,i)
		array.append(str(1))

print ''.join(array)