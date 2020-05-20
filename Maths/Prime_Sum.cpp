// https://www.interviewbit.com/problems/prime-sum/
/*
Problem:

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach’s conjecture
Example:
Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then
[a, b] < [c, d] 
If a < c OR a==c AND b < d. 
*/
#include <bits/stdc++.h>
using namespace std;
void Prime_Sum(int n)
{
	vector<int>ans;
	
	vector<int>prime(n+1,1);
	prime[0] = prime[1] = 0;

	for(int i=2; i<n+1; i++)
	{
		if(prime[i] and i*i<n+1)
		{
			for(int j=i; j<n+1; j+=i)
				prime[j]=0;
		}
	}
	for(int i=2; i<n+1; i++)
	{
		if(prime[i] and prime[n-i])
		{
			cout<<i<< " "<<n-i;
			return;
		}
	}
	return
}
int main()
{
	int n;
	cin>>n;
	vector<int>ans;
	Prime_Sum(n);
}