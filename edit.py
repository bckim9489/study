import sys
import numpy as np

op = [] #print Result List

def SUBMIN(a, b):
	return a if a < b else b

def MIN(a, b, c):
	return SUBMIN(SUBMIN(a, b), c)

def distance(S, m, T, n):
	#Metrix (m,n) = 0
	E = np.zeros((m+1, n+1))

	#init
	for i in range(0, m+1):
		E[i, 0] = i
	for j in range(0, n+1):
	 	E[0, j] = j

	#fill in metrix	
	for i in range(1, m+1):
		c1 = S[i-1]
		for j in range(1, n+1):
			c2 = T[j-1]
			if(c1 == c2):
				a = 0
			else:
				a = 1
			E[i, j] = MIN(E[i, (j-1)]+1, E[(i-1), j]+1, E[(i-1), (j-1)]+a)	 
			
	print E
	return E

def foo_sol(E, m, n):
	#Start Point -> Metrix EndPoint
	point_value = E[m, n]
	while not (m==0 and n==0):
		s = MIN(E[m, (n-1)], E[(m-1), (n-1)], E[(m-1, n)])
		
		#s == Metrix_value -> Nothing(Switch)
		if s == E[m, n]:
			c = "("+str(m)+", "+str(n)+") S"
			op.append(c)
			m = m-1
			n = n-1
		else:
			#Metrix right -> Delete
			if s == E[(m-1), n]:
				c = "("+str(m)+", "+str(n)+") D"
				op.append(c)
				m = m-1
			#Metrix diagonal -> Switch
			elif s == E[(m-1), (n-1)]:
				c = "("+str(m)+", "+str(n)+") S"
				op.append(c)
				m = m-1
				n = n-1
			#Metrix up -> Add
			else:
				c = "("+str(m)+", "+str(n)+") A"
				op.append(c)
				n = n-1
	#List Reverse
	for i in op[::-1]:
		print i

if __name__=='__main__':
	S = "strong"
	T = "stone"
	m = len(S)
	n = len(T)
	foo_sol(distance(S, m, T, n), m ,n)
#d = distance(S, m, T, n)
#print "The edit distance between {0} and {1} is {2}.".format(S, T, d)
