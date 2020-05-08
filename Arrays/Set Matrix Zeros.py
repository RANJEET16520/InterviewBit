# https://www.interviewbit.com/problems/set-matrix-zeros/

'''
Problem:
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

1 <= N, M <= 1000
0 <= A[i][j] <= 1

Example:
Input 1:
    [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]

'''
def Set_Zero(A):
	n, m = len(A), len(A[0])
	row, col = set(), set()

	for i in range(n):
		for j in range(m):
			if A[i][j] == 0:
				row.add(i)
				col.add(j)
			
	for i in row:
		for j in range(m):
			A[i][j] = 0
			
	for i in col:
		for j in range(n):
			A[j][i] = 0
	return A 

n, m = input().split()
n, m = int(n), int(m)

mat = []
for i in range(n):
	li = [int(x) for x in input().split()]
	mat.append(li)

mat = Set_Zero(mat)
for i in mat:
	print(i)