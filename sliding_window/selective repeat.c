#include<stdio.h>
int main()
{
	int windowsize,sent=0,ack,i;
	printf("enter window size\n");
	scanf("%d",&windowsize);
	while(1)
	{
		for( i = 0; i < windowsize; i++)
			{
				printf("Frame %d has been transmitted.\n",sent);
				sent++;
				if(sent == windowsize)
					break;
			}
		start:;
		printf("\nPlease enter the last Acknowledgement received.\n");
		scanf("%d", &ack);

		if (ack == windowsize)
			break;
		else
			printf("Frame %d has been transmitted.\n", ack);
		goto start;
	}
return 0;
}