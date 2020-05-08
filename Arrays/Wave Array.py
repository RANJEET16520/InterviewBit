# https://www.interviewbit.com/problems/wave-array/

'''
Problem:
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example
Given [1, 2, 3, 4]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''
def WaveArray(A):
	A.sort()
	l = len(A)//2 * 2
	for i in range(0, l, 2):
		A[i], A[i+1] = A[i+1], A[i]
	return A

a = [int(i) for i in input().split()]
print(WaveArray(a))
