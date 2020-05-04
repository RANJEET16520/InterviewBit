# https://www.interviewbit.com/problems/find-duplicate-in-array/

'''
Problem:
Given a read only array of n + 1 integers between 1 and n,
find one number that repeats in linear time using less than O(n) space
and traversing the stream sequentially O(1) times.
'''

def Duplicate(A):
	n = len(A)
	count = [0]*n
	ans = []
	for i in range(n):
		count[A[i]] += 1
		if count[A[i]] > 1:
			ans.append(A[i])
	return ans[-1] if len(ans) > 0 else -1

A = [int(x) for x in input().split()]
print(Duplicate(A))