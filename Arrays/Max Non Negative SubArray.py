# https://www.interviewbit.com/problems/max-non-negative-subarray/#
def MaxArray(A):
	ans, copy = [], []
	pre_s, s = 0, 0

	for i in range(len(A)):
		if A[i] < 0:
			s = 0
			copy = []
		else:
			s += A[i]
			copy.append(A[i])
			if pre_s < s:
				ans = copy
				pre_s = s
			elif pre_s == s and len(ans) < len(copy):
				ans = copy
	return ans


a = [int(x) for x in input().split()]
print(MaxArray(a))