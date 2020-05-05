# https://www.interviewbit.com/problems/maximum-unsorted-subarray/

'''
Problem:
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.
'''

def Maximum_Unsorted_Subarray(A):
	n = len(A)
	if n == 0:
		return [-1]

	s, e = -1, -1
	for i in range(0, n-1, 1):
		if A[i] > A[i+1]:
			s = i
			break

	if s == -1:
		return [s]

	for i in range(n-1, 0, -1):
		if A[i] < A[i-1]:
			e = i
			break

	Amin, Amax = A[s], A[s]
	for i in range(s+1, e+1, 1):
		if A[i] < Amin:
			Amin = A[i]
		elif A[i] > Amax:
			Amax = A[i]

	for i in range(0, s, 1):
		if A[i] > Amin:
			s = i
			break
	for i in range(n-1, e, -1):
		if A[i] < Amax:
			e = i
			break


	return [s, e]



A = [int(i) for i in input().split()]
print(Maximum_Unsorted_Subarray(A))