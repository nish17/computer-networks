#include <bits/stdc++.h>
using namespace std;

int main()
{

  int data[10];
  int dataR[10];

  cout << "enter data bits: ";
  cin >> data[0];
  cin >> data[1];
  cin >> data[2];
  cin >> data[4];

  data[6] = data[0] ^ data[2] ^ data[4];
  data[5] = data[0] ^ data[1] ^ data[4];
  data[3] = data[0] ^ data[1] ^ data[2];

  cout << "encoded data is:\n";
  for (int i = 0; i < 7; i++)
  {
    cout << data[i] << " ";
  }
  cout << endl;

  cout << "enter the data bits received:\n";
  for (int i = 0; i < 7; i++)
    cin >> dataR[i];

  int c1, c2, c3, c;

  c1 = dataR[6] ^ dataR[4] ^ dataR[2] ^ data[0];
  c2 = dataR[5] ^ dataR[4] ^ dataR[1] ^ data[0];
  c3 = dataR[3] ^ dataR[2] ^ dataR[1] ^ data[0];

  c = c3 * 4 + c2 * 2 + c1 * 1;
  if (c == 0)
  {
    cout << "received without error\n";
  }
  else
  {
    cout << "error on position " << c << endl;
    cout << "Data sent: ";
    for (int i = 0; i < 7; i++)
      cout << data[i] << " ";
    cout << endl;
    cout << "Data Received: ";
    for (int i = 0; i < 7; i++)
      cout << dataR[i] << " ";
    cout << endl;
  }
  return 0;
}