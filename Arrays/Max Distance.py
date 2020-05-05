# https://www.interviewbit.com/problems/max-distance/

'''
Problem:
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.
'''

def MaxDistance(A):
	n = len(A)
	if n == 0:
		return -1

	leftmin = [0]*n
	rightmax = [0]*n

	leftmin[0] = A[0]
	for i in range(1, n, 1):
		leftmin[i] = min(leftmin[i-1], A[i])

	rightmax[n-1] = A[n-1]
	for i in range(n-2, -1, -1):
		rightmax[i] = max(rightmax[i+1], A[i])

	ans = 0
	leftind = 0
	rightind = 0
	while leftind < n and rightind < n:
		if leftmin[leftind] <= rightmax[rightind]:
			ans = max(ans, rightind - leftind)
			rightind += 1
		else:
			leftind += 1

	return ans

A = [int(i) for i in input().split()]
print(MaxDistance(A))