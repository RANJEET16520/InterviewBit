# https://www.interviewbit.com/problems/anti-diagonals/

'''
Problem:
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:
Input: 	
1 2 3
4 5 6
7 8 9
Return the following :
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]

Input : 
1 2
3 4
Return the following  : 
[
  [1],
  [2, 3],
  [4]
]
'''
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
