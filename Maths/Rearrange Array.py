# https://www.interviewbit.com/problems/rearrange-array/
'''
Problem:
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Lets say N = size of the array. Then, following holds true :
1. All elements in the array are in the range [0, N-1].
2. N * N does not overflow for a signed integer.
'''

def Rearrange(A):
	n = len(A)
	if n == 0:
		return []


	for i in range(n):
		A[i] += (A[A[i]]%n)*n

	for i in range(n):
		A[i] = int(A[i]/n)
	return A

A = [int(i) for i in input().split()]
print(Rearrange(A))