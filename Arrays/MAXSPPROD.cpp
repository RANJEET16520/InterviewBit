 // https://www.interviewbit.com/problems/maxspprod/

/*
Problem:
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:

1. Leftval: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). 
If multiple A[j]’s are present in multiple positions, the Leftval is the maximum value of j.

2. Rightval: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). 
If multiple A[j]s are present in multiple positions, the Rightval is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.
Input: You will receive array of integers as argument to function.
Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the Leftval and Rightval are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
*/

#include <bits/stdc++.h>
using namespace std;

class Maxsprod
{
public:
	int ReturnMax(vector < int > &A)
	{
		int n = A.size();
		vector < int > Leftval(n,0), Rightval(n,0);	
		stack <int> st;
		st.push(0);
		
		Leftval[0] = 0;
		for(int i = 1; i < n; i++)
		{
			while(!st.empty())
			{
				if(A[st.top()] > A[i]) 
					break;
				st.pop();
			}
			Leftval[i] = (st.empty()) ? 0 : st.top();
			st.push(i);
		}

		while(!st.empty())
			st.pop();
		st.push(n-1);

		Rightval[n-1] = 0;
		for(int i = n-2; i >= 0; i--)
		{
			while(!st.empty())
			{
				if(A[st.top()] > A[i]) 
					break;
				st.pop();
			}
			Rightval[i] = (st.empty()) ? 0 : st.top();
			st.push(i);
		}

		long long int ans = -1, mod = 1000000007;

		for(int i = 0; i<n; i++)
		{
			ans = max(ans, Leftval[i] * 1LL * Rightval[i]);
		}
		return ans % mod;

	}	
};

int main()
{
	int n;
	cin >> n;

	vector < int > A;
	for(int i=0; i<n; i++)
	{
		int x;
		cin >> x;
		A.push_back(x);
	}
	Maxsprod M;
	cout << M.ReturnMax(A) << endl;
}