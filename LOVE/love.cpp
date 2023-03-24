#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int index = 0;
	const char LOVE[5] = "LOVE";
	FILE* fp; char ch;
	int k = 0; //target pattern
	int h = 0;
	char target_pattern[5] = "LOVE"; //open file
	fp = fopen("test.dat", "r"); 
	if (fp == NULL)
	{
		printf("can't open file. file is empty \n"); 
		exit(EXIT_FAILURE);
	}
	else { 
		while ((ch = fgetc(fp)) != EOF)
		{
			if (ch == 10) {
				h++;
				k = 0;
				printf("\n");
				continue;
			}
			if (ch == LOVE[index]) 
			{
				index++;
			}
			else
			{
				index = 0;
			}
			if (index == 4)
			{
				index = 0;
				printf(" %d행 %d열 에 LOVE발견\n",h,k - 3);
			}
			k++;
		}
		
		
	}
	fclose(fp);
	system("pause");
	return 0;
}