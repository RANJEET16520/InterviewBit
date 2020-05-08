# https://www.interviewbit.com/problems/spiral-order-matrix-ii/

'''
Problem:
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:
The first and the only argument contains an integer, A.

Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.

Constraints:
1 <= A <= 1000

Examples:
Input 1:
    A = 3
Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    A = 4
Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
'''
def SpiralOrder(A):
	mat = [[0 for i in range(A)] for j in range(A)]
	L, T = 0, 0
	R, B = A, A
	dirt = 0
	cnt = 0
	while L != R and T != B:
		if dirt == 0:
			for i in range(L,R,1):
				cnt += 1
				mat[T][i] = cnt
			dirt = 1
			T += 1

		elif dirt == 1:
			for i in range(T,B,1):
				cnt += 1
				mat[i][R-1] = cnt
			dirt = 2
			R -= 1

		elif dirt == 2:
			for i in range(R-1,L-1,-1):
				cnt += 1
				mat[B-1][i] = cnt
			dirt = 3
			B -= 1
			
		elif dirt == 3:
			for i in range(B-1,T-1,-1):
				cnt += 1
				mat[i][L] = cnt
			dirt = 0
			L += 1

	return mat

a = int(input())
print(SpiralOrder(a))
