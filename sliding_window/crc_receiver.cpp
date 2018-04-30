// #include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
  string crc, encoded;
  cout << "Enter the message\n";
  getline(cin, encoded);
  cout << "Enter the crc generator\n";
  getline(cin, crc);
  // int m = msg.length();
  int n = crc.length();
  for (int i = 0; i <= encoded.length() - n;)
  {
    for (int j = 0; j < n; j++)
    {
      encoded[i + j] = encoded[i + j] == crc[j] ? '0' : '1';
    }
    for (; i < encoded.length() && encoded[i] != '1'; i++)
      ;
  }
  for (char i : encoded.substr(encoded.length() - crc.length()))
    if (i != '0')
    {
      cout << "Error!\n";
      return 0;
    }
  cout << "No error\n";

  return 0;
}