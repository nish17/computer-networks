#include <iostream>
using namespace std;

int main()
{
  int window, sent = 0, ask;
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
    cout << "Enter the last ack received\n";
    cin >> ask;
    if (window == ask)
      break;
    else
      sent = ask;
  }
  return 0;
}