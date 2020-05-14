# https://www.interviewbit.com/problems/excel-column-number/

'''
Problem:
Given a column title as appears in an Excel sheet, return its corresponding column number.
A -> 1
B -> 2
C -> 3
........
Z -> 26
AA -> 27
AB -> 28 
'''

def Excel(A):
	n = len(A)

	if n == 0:
		return 0
	if n == 1:
		return ord(A)-65+1

	else:
		ans = 0
		for i in range(n-1):
			x = ord(A[i])-65+1
			ans += 26 ** (n-1-i)* x

		ans += ord(A[n-1])-65+1
	return ans

A = input()
print(Excel(A))