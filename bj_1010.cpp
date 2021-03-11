#include <stdio.h>

int dp[40][40];
int ft_dp(int n, int m);
int main()
{
    int t, n, m;
    scanf("%d", &t);

    for(int i = 0;i<40;i++)
        for(int j=0;j<40;j++)
            dp[i][j]=0;
    
    for(int i = 0 ; i < 40 ; i++){
        dp[i][i] = 1;
        dp[i][0] = 1;
    }
    while(t--)
    {
        scanf("%d %d", &n, &m);
        printf("%d\n", ft_dp(n,m));
    }
    return (0);
}

int ft_dp(int n, int m)
{
    if(dp[m][n] == 0)
        dp[m][n] = ft_dp(n, m-1) + ft_dp(n-1, m-1);
    return (dp[m][n]);
}