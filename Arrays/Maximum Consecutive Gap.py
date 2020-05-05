# https://www.interviewbit.com/problems/maximum-consecutive-gap/

'''
Problem:
Given an unsorted array, find the maximum difference
between the successive elements in its sorted form.
Try to solve it in linear time/space.

Example :
Input : [1, 10, 5]
Output : 5 
'''
def Gap(A):
	ans = -1
	n = len(A)
	if n <= 2:
		return 0

	A.sort()
	for i in range(1,n):
		diff = A[i] - A[i-1]
		if ans < diff:
			ans = diff

	return ans

A = [int(x) for x in input().split()]
print(Gap(A))