#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int swap_num(int, int);

int main(void)
{
	int i, j, k;
	int n, m;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &m);
		printf("Pairs for %d: ", m);
		for (j = 1; j < 12; j++)
		{
			for (k = 1; k < 12; k++)
			{
				if (j + k == m)
					if (j <= k)
					{
						if (j - k == 0)
							continue;
						if (j == 1)
							printf("%d %d", j, k);
						else
							printf(", %d %d", j, k);
					}
			}
		}
		printf("\n");
	}
	return 0;
}