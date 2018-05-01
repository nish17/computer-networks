#include <bits/stdc++.h>
using namespace std;

int main()
{
  char a[20], b[20], sum[20], comp[20];
  cout << "Enter first binary string\n";
  cin >> a;
  cout << "Enter second binary string\n";
  cin >> b;

  if (strlen(a) == strlen(b))
  {
    char carry = '0';
    int length = strlen(a);

    for (int i = length - 1; i >= 0; i--)
    {
      if (a[i] == '0' && b[i] == '0' && carry == '0')
      {
        carry = '0';
        sum[i] = '0';
      }
      else if (a[i] == '0' && b[i] == '0' && carry == '1')
      {
        sum[i] = '1';
        carry = '0';
      }
      else if (a[i] == '0' && b[i] == '1' && carry == '0')
      {
        sum[i] = '1';
        carry = '0';
      }
      else if (a[i] == '0' && b[i] == '1' && carry == '1')
      {
        sum[i] = '0';
        carry = '1';
      }
      else if (a[i] == '1' && b[i] == '0' && carry == '0')
      {
        sum[i] = '1';
        carry = '0';
      }
      else if (a[i] == '1' && b[i] == '0' && carry == '1')
      {
        sum[i] = '0';
        carry = '1';
      }
      else if (a[i] == '1' && b[i] == '1' && carry == '0')
      {
        sum[i] = '0';
        carry = '1';
      }
      else if (a[i] == '1' && b[i] == '1' && carry == '1')
      {
        sum[i] = '1';
        carry = '1';
      }
      else
        break;
    }
    cout << "sum: " << carry << sum << endl;
    for (int i = 0; i < length; i++)
    {
      comp[i] = sum[i] == '0' ? '1' : '0';
      carry = carry == '1' ? '0' : '0';
    }

    cout << "checksum: " << carry << comp << endl;
  }

  return 0;
}