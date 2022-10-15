#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int n_zombie, r_zombie;
		scanf("%d %d", &n_zombie, &r_zombie);
		if (n_zombie >= r_zombie)
			printf("MMM BRAINS\n");
		else
			printf("NO BRAINS\n");
	}

	return 0;
}