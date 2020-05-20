# https://www.interviewbit.com/problems/power-of-two-integers/
'''
Problem:
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
Example
Input : 4
Output : True  
as 2^2 = 4. 
'''
def isPower(A):
	n = A
	for i in range(2,int(n**0.5)+1):
		y = 2
		p = int(i**y)
		while(p<=n and p>0):
			if p==n:
				return i, y
			y+=1
			p = int(i**y)
	return 0

n = int(input())
print(isPower(n))