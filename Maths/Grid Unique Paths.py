# https://www.interviewbit.com/problems/grid-unique-paths/

'''
Problem:
The problem is to count all the possible paths from top left to bottom right of a mXn matrix.
'''

def UniquePath(A,B):
	'''
	# Recursion:
	if A == 0 and B == 0:
		return 0
	if A == 1 or B == 1:
		return 1
	return UniquePath(A-1, B) + UniquePath(A, B-1) 
	'''


	
	# DP:
	ans = [[0 for i in range(B)] for j in range(A)]

	for i in range(A):
		ans[i][0] = 1
	for i in range(B):
		ans[0][i] = 1

	for i in range(1, A):
		for j in range(1, B):
			ans[i][j] = ans[i-1][j] + ans[i][j-1]
	
	# for i in range(A):
	# 	print(ans[i])

	return ans[A-1][B-1]
	

	'''
	# Mathematical Solution:
	fact = [0]

	for i in range(1,A+B-1):
		if i == 1:
			fact.append(1)
		else:
			fact.append(i*fact[-1])
	# print(fact)
	ans = fact[-1]//(fact[A-1]*fact[B-1])
	return ans
	'''

	'''
	from math import factorial as f
	def nCr(n,r):
		return f(n)//(f(r)*f(n-r))
	def uniquePaths(self, A, B):
		return nCr((A+B-2),A-1)
	'''
	

A, B = input().split()
A, B = int(A), int(B)
print(UniquePath(A, B))