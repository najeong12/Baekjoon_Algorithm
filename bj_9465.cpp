#include <stdio.h>
#include <algorithm>

int dp[2][100001], a[2][100001];
int main(){
    int t, n, i, j;   
    scanf("%d", &t);

    while(t--)
    {
        scanf("%d", &n);
		for (i = 0; i <= 1; i++)
			for (j = 1; j <= n; j++) 
				scanf("%d", &a[i][j]);

		dp[0][0] = dp[1][0] = 0;
		dp[0][1] = a[0][1];	
        dp[1][1] = a[1][1];

		for (i = 2; i <= n; i++) {
			dp[0][i] = std::max(dp[1][i - 1], dp[1][i - 2]) + a[0][i];
			dp[1][i] = std::max(dp[0][i - 1], dp[0][i - 2]) + a[1][i];
		}
		printf("%d\n", std::max(dp[0][n], dp[1][n]));
    }
    return (0);
}