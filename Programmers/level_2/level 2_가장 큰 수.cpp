#include <string>
#include <vector>
#include <algorithm>
using namespace std;


bool cmp(const string& x, const string& y);

string solution(vector<int> numbers) {
	vector<string> numbers2;
	string answer = "";
	for (int i = 0; i < numbers.size(); i++) {
		numbers2.push_back(to_string(numbers[i]));
	}
	sort(numbers2.begin(), numbers2.end(), cmp);
	for (int i = 0; i < numbers2.size(); i++) {
		answer += numbers2[i];
	}

	if (answer[0] == '0')
		return "0";
	return answer;
}

bool cmp(const string& x, const string& y) {
	if ((x + y) > (y + x)) return 1;
	else return 0;
}