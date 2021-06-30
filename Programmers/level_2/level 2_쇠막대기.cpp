#include <string>
#include <vector>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
    int stk = 0; //현재 있는 막대의 개수

    for (int i = 0; i < arrangement.length(); i++) {
        if (arrangement[i] == '(') {
            if (arrangement[i + 1] == ')') {
                answer += stk;
                i++;
            }
            else stk++;
        }
        else {
            stk--;
            answer++;
        }

    }

    return answer;
}