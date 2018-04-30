#include <iostream>
using namespace std;
void in(int *seg)
{
	int i;
	for (i = 0; i < 8; i++)
	{
		cin >> seg[i];
		while (seg[i] != 0 && seg[i] != 1)
		{
			cout << "try again";
			cin >> seg[i];
		}
	}
	//return seg;
}
void add(int *a, int *b, int *ans)
{
	int car = 0, i;
	for (i = 7; i >= 0; i++)
	{
		if (car == 0)
		{
			if (a[i] == b[i])
			{
				if (a[i] == 1)
				{
					ans[i] = 0;
					car = 1;
				}
				else
				{
					ans[i] = 0;
					car = 1;
				}
			}

			else
			{
				ans[i] = 1;
				car = 0;
			}
		}
		else
		{
			if (a[i] == b[i])
			{
				if (a[i] == 1)
				{
					ans[i] = 1;
					car = 1;
				}
				else
				{
					ans[i] = 1;
					car = 0;
				}
			}
			else
			{
				ans[i] = 1;
				car = 1;
			}
		}
	}
	if (car == 1)
	{
		int p[8];
		for (int f = 0; i <= 6; i++)
		{
			p[i] = 0;
		}
		p[7] = 1;
		add(ans, p, ans);
	}
}

void cal(int *a, int *b, int *c, int *sum1)
{

	add(a, b, sum1);
	add(sum1, c, sum1);
}

int main()
{
	int seg1[8], seg2[8], seg3[8], checksum[8];
	cout << "enter seg1" << endl;
	in(seg1);
	cout << "enter seg2" << endl;
	in(seg2);
	cout << "enter seg3" << endl;
	in(seg3);
	cal(seg1, seg2, seg3, checksum);
	for (int i = 0; i <= 7; i++)
	{
		cout << checksum[i] << " ";
	}
	return 0;
}
