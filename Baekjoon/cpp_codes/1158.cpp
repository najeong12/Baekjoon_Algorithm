#include <iostream>
#include <vector>

int N, K;
std::vector <int> answer;
std::vector <int> visited;

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
    std::cin >> N >> K;
    visited.resize(N+1, 0);
}

void solve()
{
    int num = K;
    answer.push_back(num);
    visited[num] = 1;
    while (answer.size() < N){
        int cycle = 0;
        while (cycle < K){
            num = (num == N) ? 1 : num+1;
            if (visited[num] == 0)
                cycle += 1;
        }
        answer.push_back(num);
        visited[num] = 1;
    }
}

void print_val()
{
    std::cout << '<';
    for(int i = 0 ; i < N ; i++){
        if (i != N-1)
            std::cout << answer[i] << ", ";
        else
            std::cout << answer[i];
    }
    std::cout << ">";
}

int main()
{
	input_faster();
	input();
	solve();
	print_val();
	return (0);
}
