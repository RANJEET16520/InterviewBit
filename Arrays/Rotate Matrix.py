# https://www.interviewbit.com/problems/rotate-A/

'''
Problem:
You are given an n x n 2D A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note that if you end up using an additional array, you will only receive partial score.

Example:
If the array is
[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]

'''
def Rotate(A):
	n = len(A)
	if n == 0:
		return []

	ans = [[0 for j in range(n)] for i in range(n)]

	for i in range(n):
		for j in range(n):
			ans[j][n-1-i] = A[i][j]

	return ans

n = int(input())
mat = []

for i in range(n):
	row = [int(i) for i in input().split()]
	mat.append(row)

print(Rotate(mat))