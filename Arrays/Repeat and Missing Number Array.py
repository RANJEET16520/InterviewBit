# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

'''
Problem:
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
'''

def repeatedNumber(A):
	size = len(A) + 1
	count = [0] * size

	for val in A:
		count[val] += 1
		res1 = 0
		res2 = 0

	for idx, val in enumerate(count):
		if val == 2:
			res1 = idx
		if val == 0:
			res2 = idx

	return res1, res2

A = [int(i) for i in input().split()]
print(repeatedNumber(A))