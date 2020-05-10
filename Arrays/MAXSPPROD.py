# https://www.interviewbit.com/problems/maxspprod/

'''
Problem:
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:

1. LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). 
If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.

2. RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). 
If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.
Input: You will receive array of integers as argument to function.
Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
'''
def Maxsprod(A):
	mod = 1000000007
	n = len(A)
	if n<3:
		return 0
	rightspval = [0]*n
	leftspval = [0]*n
	stack = []
	
	stack.append(0)
	for i in range(1,n):
		while stack and A[stack[-1]] < A[i]:
			rightspval[stack.pop()] = i
		stack.append(i)
	stack = []
	
	stack.append(n-1)
	for i in range(n-1,-1,-1):
		while stack and A[stack[-1]] < A[i]:
			leftspval[stack.pop()] = i
		stack.append(i)
	del(stack)
	
	ans = -1
	for i in range(n):
		ans = max(ans, leftspval[i]*rightspval[i])
	return ans%mod

A = [int(x) for x in input().split()]
print(Maxsprod(A))