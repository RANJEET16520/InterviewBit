# https://www.interviewbit.com/problems/excel-column-title/

'''
Problem:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
1 -> A
2 -> B
3 -> C
......
26 -> Z
27 -> AA
28 -> AB 
'''

def Excel(A):
	if A == 0:
		return 0
	else:
		ans = ""
		while A > 0:
			x = A % 26
			if x == 0:
				x = 26
				A -= 1
			ans += chr(64+x)
			A //= 26
			
		ans = ans[::-1]
		return ans

A = int(input())
print(Excel(A))