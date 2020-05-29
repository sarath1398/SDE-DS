/*                                                    FRACTIONAL KNAPSACK                                                            */

#include<bits/stdc++.h>
using namespace std;
void swap(int *x,int *y)
{
	int temp=*x;
	*x=*y;
	*y=temp;
}
int main()
{
	//Fast I/O Functions
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n;
	cin>>n;
	int weights[n],cost[n],ratio[n];
	for(int i=0;i<n;i++)
	{
		cin>>cost[i]>>weights[i];
		ratio[i]=cost[i]/weights[i];
	}
	int capacity;
	cin>>capacity;
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			if(ratio[i]<ratio[j])
			{
				swap(ratio[i],ratio[j]);
				swap(cost[i],cost[j]);
				swap(weights[i],weights[j]);
			}
		}
	}
	for(int i=0;i<n;i++)
	{
		cout<<ratio[i]<<' '<<cost[i]<<' '<<weights[i]<<' ';
	}
	int i=0,max_capacity=0;
	while(capacity)
	{
		if(capacity>weights[i])
		{
			capacity-=weights[i];
			max_capacity+=cost[i];
		}
		else
		{
			max_capacity+=(int)(((float)capacity/(float)weights[i])*cost[i]);
			break;
		}
		//cout<<max_capacity;
		++i;
	}
	cout<<max_capacity;
}
