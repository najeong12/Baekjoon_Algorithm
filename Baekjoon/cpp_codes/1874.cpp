#include <iostream>
#include <vector>

int N;
std::vector<int> arr;
std::vector<char> result;
std::vector<int> temp;

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
	std::cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a;
        std::cin >> a;
        arr.push_back(a);
    }
}

void solve()
{
    int j = 0;
    for (int i = 1 ; i < N + 1 ; i++){
        temp.push_back(i);
        result.push_back('+');
        while (!temp.empty() && temp.back() == arr[j]){
            temp.pop_back();
            j++;
            result.push_back('-');
        }
    }
}

void print_val()
{
    if (temp.empty()){
        for (int i = 0 ;i < result.size();i++)
            std::cout << result[i] << std::endl;
    }
    else
        std::cout << "NO";
}

int main()
{
	input_faster();
	input();
	solve();
	print_val();
	return (0);
}