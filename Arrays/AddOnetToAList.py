# https://www.interviewbit.com/problems/add-one-to-number/

'''
Problem:
Given a non-negative number represented as an array of digits,
add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.

Example:
If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]
as 123 + 1 = 124.
'''
def plusOne(A):
	x = 1
	for i in range(len(A)-1, -1, -1):
		x = x + A[i]
		bor = int(x/10)
		if bor == 0:
			A[i] = x
			x = 0
		else:
			A[i] = x%10
			x = 1
	A = [bor] + A
	while A[0]==0:
		del A[0]
	return A
		
A = [int(i) for i in input().split()]
print(plusOne(A))