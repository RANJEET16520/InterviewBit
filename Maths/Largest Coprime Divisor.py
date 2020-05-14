# https://www.interviewbit.com/problems/largest-coprime-divisor/

'''
Problem:
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
1. X divides A i.e. A % X = 0
2. X and B are co-prime i.e. gcd(X, B) = 1

For example,
A = 30
B = 12
We return
X = 5

'''

def gcd(a, b):
	if b > a:
		b, a = a, b
	while b:
		a, b = b, a % b
	return a

def Largest_Coprime(self, A, B):
	x = gcd(A, B) 
	while x > 1:
		A = A // x  
		x = gcd(A, x)
	return A  


A, B = input().split()
A, B = int(A), int(B)
print(Largest_Coprime(A, B))
		