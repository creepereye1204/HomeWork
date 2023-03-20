#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include<vector>
#include<iostream>
using namespace std;
int main()
{
	vector<int>::iterator iter; // vector 반복자 iter 선언
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
	else { // 파일을 읽어 A 배열에 저장
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
		cout <<"index:\t"<<*iter <<"번째에 LOVE가 존재합니다."<< endl;
	}
	system("pause");
	return 0;
}