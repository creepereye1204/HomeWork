#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include<vector>
#include<iostream>
using namespace std;
int main()
{
	vector<int>::iterator iter; // vector �ݺ��� iter ����
	vector<int> result;
	int index = 0;
	const char LOVE[5] = "LOVE";
	FILE* fp; char ch;
	int k = 0; //target pattern
	char target_pattern[5] = "LOVE"; //open file
	fp = fopen("test.dat", "r"); 
	if (fp == NULL)
	{
		printf("can't open file. file is empty \n"); 
		exit(EXIT_FAILURE);
	}
	else { // ������ �о� A �迭�� ����
		while ((ch = fgetc(fp)) != EOF)
		{
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
				result.push_back(k - 3);
			}
			k++;
		}
		
		
	}
	fclose(fp);
	for (iter = result.begin(); iter != result.end(); iter++) 
	{
		cout <<"index:\t"<<*iter <<"��°�� LOVE�� �����մϴ�."<< endl;
	}
	system("pause");
	return 0;
}