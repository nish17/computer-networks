#include <iostream>
using namespace std;

int main()
{
  string msg, crc, encoded;
  cout << "Enter the message\n";
  getline(cin, msg);
  cout << "enter the crc\n";
  getline(cin, crc);
  int m = msg.length(), n = crc.length();
  encoded += msg;
  for (int i = 0; i < n - 1; i++)
    encoded += '0';
  for (int i = 0; i <= encoded.length() - n;)
  {
    for (int j = 0; j < n; j++)
      encoded[i + j] = encoded[i + j] == crc[j] ? '0' : '1';
    for (; i < encoded.length() && encoded[i] != '1'; i++)
      ;
  }
  for (char i : encoded.substr(encoded.length() - crc.length()))

    if (i != '0')
    {
      cout << "error!";
      return 0;
    }
    else
    {
      cout << "no error\n";
      return 0;
    }
}