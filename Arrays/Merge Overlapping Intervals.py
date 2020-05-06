# https://www.interviewbit.com/problems/merge-overlapping-intervals/

'''
Problem:
Merge Overlapping Intervals
Given a collection of intervals, merge all overlapping intervals.

For example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''
def MergeIntervals(intervals):
	res = []
	intervals.sort(key=lambda i: i[0])
	for i in intervals:
		if not res or res[-1][1] < i[0]:
			res.append(i)
		else:
			res[-1][1] = max(res[-1][1], i[1])
	return res

inp_list = [int(i) for i in input().split()]
intervals = []

for i in range(0, len(inp_list), 2):
	x = []
	x.append(inp_list[i])
	x.append(inp_list[i+1])
	
	intervals.append(x)
print(MergeIntervals(intervals))
