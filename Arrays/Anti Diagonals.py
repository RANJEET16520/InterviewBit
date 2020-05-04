# https://www.interviewbit.com/problems/anti-diagonals/

def AntiDiagonals(A):
	mat = []
	if len(A) == 1:
		return [[0]]
	n = len(A[0])
	for i in range(n):
		k = 0
		lis = []
		for j in range(i, -1, -1):
			lis.append(A[k][j])
			k += 1
		mat.append(lis)

	for i in range(n-1):
		k = n-1
		lis = []
		for j in range(i+1, n, 1):
			lis.append(A[j][k])
			k -= 1
		mat.append(lis)

	return mat

n = int(input())
mat = []

for i in range(n):
	lis = [int(j) for j in input().split()]
	mat.append(lis)

mat = AntiDiagonals(mat)
for i in mat:
	print(i)
