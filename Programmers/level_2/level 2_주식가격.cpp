#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;  // 정답을 저장하는 vector

    for (int i = 0; i < prices.size(); i++) {
        int ch = 0;  //자신보다 높은 가격을 가지는 초를 저장하기 위한 변수
        for (int j = i + 1; j < prices.size(); j++) {
            if (prices[i] <= prices[j]) ch++;
            else {
                ch++;
                break;
            }
        }
        answer.push_back(ch);
    }
    return answer;
}