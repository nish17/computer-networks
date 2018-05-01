#include <stdio.h>
// #include <bios.h>
// #include <conio.h>
#define COM1 0
#define SETTINGS 0x82
#define DTR 0x100
void main()
{
  int ch, status, i = 0, true = 1;
  char msg[100], ack, rec;
  clrscr();
  bioscom(0, SETTINGS, COM1);
  printf("\n 1.Transmit\n 2.Receive");
  printf("\n\n Enter the operation code : ");
  scanf("%d", &ch);
  switch (ch)
  {
  case 1:
    printf("\n Enter the Message \n ");
    scanf("%s", &msg);
    while (msg[i] != '\0')
    {
      bioscom(1, msg[i], COM1);
      printf("\n%c", msg[i]);
      do
      {
        while (1)
        {
          status = bioscom(3, 0, COM1);
          if (status & DTR)
          {
            ack = bioscom(2, 0, COM1) & 0x7F;
            if (ack == '0')
            {
              bioscom(1, msg[i], COM1);
              printf("\n%c - retransmitted ", msg[i]);
            }
            break;
          }
        }
      } while (ack != '1');
      i++;
    }
    break;
  case 2:
    printf("\n Receiver \t Press Escape to quit\n\n");
    do
    {
      status = bioscom(3, 0, COM1);
      if (status & DTR)
      {
        rec = bioscom(2, 0, COM1);
        printf("\n%c  -- Enter ACK(1 for +ve, 0 for -ve) :", rec);
        ack = getche();
        bioscom(1, ack, COM1);
      }
      if (kbhit())
        if (getch() == '\x1b')
          true = 0;
    } while (true);
    break;
  default:
    printf("\n Invalid Selection");
  }
}
