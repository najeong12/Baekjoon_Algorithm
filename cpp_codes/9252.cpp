#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

std::vector<std::vector<int> > dp;
std::vector<char> answer;
std::string str1, str2;

void preset()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);
}

void init(){
	std::cin >> str1 >> str2;
	dp.resize(str1.length()+1, std::vector<int>(str2.length()+1,0));
}

void solution(){
	//fill dp
	for (int i = 1 ; i <= str1.length() ; i++){
		for(int j = 1 ; j<= str2.length() ; j++){
			if (str1[i-1] == str2[j-1])
				dp[i][j] = dp[i-1][j-1] + 1;
			else
				dp[i][j] = std::max(dp[i-1][j], dp[i][j-1]);
		}
	}
	//fill answer
	int i = str1.length();
	int k = str1.length();
	for(int j = str2.length(); j>=0 ; j--){
		if (dp[i][j] == 0)
			break;
		for (int i = k; i>=0 ; i--){
			if (dp[i][j] == dp[i][j-1])
				break;
			else if (dp[i][j] == dp[i-1][j])
				continue;
			else{
				answer.push_back(str1[i-1]);
				k = i-1;
				break;	
			}
		}
	}
}

void output(){
	std::cout << answer.size() << std::endl;
	while(!answer.empty()){
		std::cout << answer.back();
		answer.pop_back();
	}
	std::cout << std::endl;
}

int main(){
	preset();
	init();
	solution();
	output();
	return (0);
}
