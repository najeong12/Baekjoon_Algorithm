#include <iostream>
#include <algorithm>

int N, M;
int dp[1001][1001];
int candy[1001][1001];

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
	std::cin >> N >> M;
	for (int i = 1 ; i <= N ; i++)
		for (int j = 1; j <= M ; j++)
			std::cin >> candy[i][j];
}

void solve()
{
	for (int i = 1 ; i <= N ; i++)
		for (int j = 1 ; j <= M ; j++)
			dp[i][j] = std::max(std::max(dp[i - 1][j - 1], dp[i - 1][j]), dp[i][j - 1]) + candy[i][j];
}

void print_val()
{
	std::cout << dp[N][M];
}

int main()
{
    input_faster();
	input();
	solve();
	print_val();
	return (0);
}