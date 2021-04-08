#include <iostream>
#include <stack>

int N;
int M;
int V;
std::vector <int> arr[1000];
int visited[1001] = {0 , };

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
    int x;
    int y;
    std::cin >> N >> M >> V;
    while (M--){
        std::cin >> x >> y;
        arr[x].push_back(y);
        arr[y].push_back(x);
    }
}

void dfs(int V)
{
    printf("%d ", V);
    visited[V] = 1;
    for(int next : arr[V])
        if (visited)
}

void bfs(int V)
{
    
}

void print_val()
{
  dfs(V);
  bfs(V);
}

int main()
{   
	input_faster();
	input();
	print_val();
	return (0);
}