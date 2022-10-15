/* #define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

 int main(void)
{
	int number[3];
	int i, j, temp;
	for (i = 0; i < 3; i++)			// number 배열에 들어갈 수를 입력받는 반복문
	{
		scanf("%d", &number[i]);
	}
	for (i = 0; i < 2; i++)		    // number 배열안의 수를 비교하여 오름차순으로 정리
		for (j = 1; j < 3; j++)
		{
			if (number[i] > number[j])
			{
				temp = number[j];
				number[j] = number[i];
				number[i] = temp;
			}
		}
	for (i = 0; i < 3; i++)			// number 배열안의 요소 출력
	{
		printf("%d ", number[i]);
	}

	return 0;
} 
int main(void)
{
	int a, b, c, temp;
	scanf("%d %d %d", &a, &b, &c);
	if (a > b) {
		temp = a; a = b; b = temp; // temp에 a값 저장, a,b값 바뀜
	}
	if (b > c) {
		temp = b; b = c; c = temp; // temp에 b값 저장, b,c 값 바뀜
	}
	if (a > b) {
		temp = a; a = b; b = temp; // temp에 a값 저장, a,b 값 바뀜
	}		

	printf("%d %d %d", a, b, c);
} */