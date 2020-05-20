# https://www.interviewbit.com/problems/palindrome-integer/
'''
Problem:
Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.
'''
def PalindromeInteger(A):
	A = str(A)
	n = len(A)
	if n == 0:
		return 1

	for i in range(n):
		if A[n-1-i] != A[i]:
			return 0

	return 1 

A = input()
print(PalindromeInteger(A))