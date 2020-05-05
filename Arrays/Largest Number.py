# https://www.interviewbit.com/problems/largest-number/

'''
Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
'''
from functools import cmp_to_key

def Largest(A):
	A = [str(i) for i in A]
	cmpr = cmp_to_key(lambda a,b: 1 if int(a+b) >= int(b+a) else -1)
	A.sort(key = cmpr, reverse=True)
	res = ''.join(A)
	res = res.lstrip('0')
	return res if res else '0'

a = [int(x) for x in input().split()]
print(Largest(a))

