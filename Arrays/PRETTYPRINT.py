# https://www.interviewbit.com/problems/prettyprint/

'''
Problem:
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:
Input: A = 4.
Output:
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Example 2:
Input: A = 3.
Output:
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
'''
def PrettyPrint(A):
	if A == 0:
		return []
	mat = [[0 for i in range(2*A-1)] for j in range(2*A-1)]

	i = 0
	for i in range(0, A):
		for j in range(i, 2*A-1-i):
			mat[i][j] = A-i
			mat[j][i] = A-i
			mat[2*(A-1)-i][j] = A-i
			mat[j][2*(A-1)-i] = A-i
	return mat

A = int(input())
mat = PrettyPrint(A)
for i in mat:
	print(i)