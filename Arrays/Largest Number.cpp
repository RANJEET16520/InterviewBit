 // https://www.interviewbit.com/problems/largest-number/

/*
Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
*/

#include <bits/stdc++.h>
using namespace std;

class Largest_Number
{
public:
	static bool cmpr(string a, string b)
	{
		return(a+b > b+a);
	}

	string Find(vector < int > & A)
	{
		vector<string>ans;
		int n = A.size();
		if (n == 0)
			return "0";
		for(int i=0; i<n; i++)
		{
			int val = A[i];
			string str = "";
			if (val > 0)
			{
				while(val > 0)
				{
					int r = val%10;
					str += char(r + 48);
					val /= 10;
				}
			}
			else
				str += char(val + 48);
			reverse(str.begin(), str.end());
			ans.push_back(str);

			// cout<<str<<endl;
		}

		sort(ans.begin(), ans.end(), cmpr);

		string sol = "";
		int cnt = 0;
		for(auto itr = ans.begin(); itr != ans.end(); itr++)
		{
			sol += *itr;
			if (*itr == "0")
				cnt += 1;
		}
		if (cnt == n)
			return "0";
		return sol;
	}

	
};
int main()
{
	vector<int>vect;
	int n; 

	cin >> n;
	for(int i = 0; i<n; i++)
	{
		int x;
		cin>>x;
		vect.push_back(x);
	}

	Largest_Number L;
	cout << L.Find(vect);

}

