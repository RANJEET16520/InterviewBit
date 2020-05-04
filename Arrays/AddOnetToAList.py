# https://www.interviewbit.com/problems/add-one-to-number/
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