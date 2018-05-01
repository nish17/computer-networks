#include <iostream>
using namespace std;

int main()
{

  int window, sent = 0, ack;
  cout << "enter window size\n";
  cin >> window;
  while (1)
  {
    for (int i = 0; i < window; i++)
    {
      cout << "Frame " << i << " has been transmitted\n";
      sent++;
      if (sent == window)
        break;
    }
  start:;
    cout << "enter the last acknolegdement you received\n";
    cin >> ack;
    if (ack == window)
      break;
    else
      cout << "Frame " << ack << " has been transmitted\n";
    goto start;
  }
  return 0;
}