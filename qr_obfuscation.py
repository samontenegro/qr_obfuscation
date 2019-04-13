import numpy as np 

N=21
w_b = '\u2591\u2591'
b_b = '\u2588\u2588'

def delta(i,j):
	if i == j:
		a = 1
	elif i != j:
		a = 0
	return a

def elem_swap(m,n):
	A = []
	for i in range(0,N):
		B = N*[0]
		for j in range(0,N):
			v = delta(i,j)*(1-delta(i,m))*(1-delta(i,n)) + delta(i,m)*delta(j,n) + delta(i,n)*delta(j,m)
			B[j] = v
		A.append(B)
	A = np.array(A,dtype="int32")
	return A

def iden():
	A = []
	for i in range(0,N):
		B = N*[0]
		for j in range(0,N):
			v = delta(i,j)
			B[j] = v
		A.append(B)
	A = np.array(A,dtype="int32")
	return A

def elem_add(m,n):
	A = []
	for i in range(0,N):
		B = N*[0]
		for j in range(0,N):
			v = delta(i,j) + delta(i,m)*delta(j,n)
			B[j] = v
		A.append(B)
	A = np.array(A,dtype="int32")
	return A

def index_rchoice():
	a = np.random.choice(range(0,N),2,replace=False)
	return a

def qrprint(arr):
	line = ""
	for i in range(0,N):
		for j in range(0,N):
			if arr[i][j] == 0:
				line = line + '\u2591\u2591'
			elif arr[i][j] == 1:
				line = line + '\u2588\u2588'
		print(line)
		line = ""

def qrprint_f(arr1,arr2,arr3):
	line = ""
	for i in range(0,N):
		for j in range(0,N):
			if arr1[i][j] == 0:
				line = line + '\u2591\u2591'
			elif arr1[i][j] == 1:
				line = line + '\u2588\u2588'
		line = line + "  "

		for z in range(0,N):
			if arr2[i][z] == 0:
				line = line + '\u2591\u2591'
			elif arr2[i][z] == 1:
				line = line + '\u2588\u2588'
		line = line + "  "

		for n in range(0,N):
			if arr3[i][n] == 0:
				line = line + '\u2591\u2591'
			elif arr3[i][n] == 1:
				line = line + '\u2588\u2588'
		print(line)
		line = ""		


qr = np.array([
[0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0],
[0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0],
[0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,0],
[0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0],
[0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1],
[0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,0,1],
[0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0],
[1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1],
[1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1],
[0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,1],
[0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1],
[0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1],
[0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1],
[0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1],
[0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1],
[0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1],
], dtype="int32")

ops = []

qrprint(qr)
print('\n OBFUSCATED BARCODE \n')

for l in range(0,1000):
	m,n = index_rchoice()
	if np.random.sample() < 1:
		eadd = elem_add(m,n)
		qr = np.dot(eadd,qr)
		ops.append(eadd)
	else:
		eswap = elem_swap(m,n)
		qr = np.dot(eswap,qr)
		ops.append(eswap)

qr = qr % 2

qrprint(qr)

print('\n KEY MATRIX \n')


key = ops.reverse()
keymat = iden()

for m in range(len(ops)):
	keymat = np.dot(ops[m],keymat)
keymat = keymat % 2

qrprint(keymat)

print('\n CONFIRMATION \n')

verf = np.dot(keymat,qr)
verf = verf % 2

qrprint(verf)

if verf.all() == qr.all():
	print('\n MATRIX VERIFIED \n')
	print('\n END RESULT \n')

	qrprint_f(keymat,qr,verf)