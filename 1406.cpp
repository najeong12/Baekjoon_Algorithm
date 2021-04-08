#include <iostream>
#include <stack>

int N;
std::stack <char> left;
std::stack <char> right; 
std::stack <char> tmp;

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
    std::string str;
    std::cin >> str;
    for(int i = 0; i < str.size() ; i++){
        left.push(str[i]);
    }
    std::cin >> N;
}

void solve()
{
    char func;
    while (N--){
        std::cin >> func;
        if (func == 'P'){
            char x;
            std::cin >> x;
            left.push(x);
        }
        else if (func == 'L'){
            if (!left.empty()){
                right.push(left.top());
                left.pop();
            }
        }
        else if (func == 'B'){
            if (!left.empty())
                left.pop();
        }
        else if (func == 'D'){
            if (!right.empty()){
                left.push(right.top());
                right.pop();
            }
        }
    }
}

void print_val()
{
   while (!left.empty()){
       tmp.push(left.top());
       left.pop();
   }
   while (!tmp.empty()){
       std::cout << tmp.top();
       tmp.pop();
   }
   while (!right.empty()){
       std::cout << right.top();
       right.pop();
   }
}

int main()
{
	input_faster();
	input();
	solve();
	print_val();
	return (0);
}