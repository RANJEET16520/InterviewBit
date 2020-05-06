# https://www.interviewbit.com/problems/pascal-triangle/

'''
Problem:

Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,
Return
[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
'''
def PascalTriangle(A):
	mat = []

	for i in range(A):
		lis = []

		if i == 0:
			lis.append(1)
		else: 
			pre_lis = mat[-1]

			for j in range(i+1):
				if j == 0:
					lis.append(pre_lis[j])
				elif j == i:
					lis.append(pre_lis[-1])
				else:
					lis.append(pre_lis[j-1] + pre_lis[j])

		mat.append(lis)

	return mat
a = int(input())
mat = PascalTriangle(a)
for i in mat:
	print(i)
