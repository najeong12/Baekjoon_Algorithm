#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    answer = s;

    for (int i = 0; i < answer.length() - 1; i++) {
        for (int j = 0; j < answer.length(); j++) {
            if (answer[j] < answer[j + 1]) {
                char tmp;
                tmp = answer[j];
                answer[j] = answer[j + 1];
                answer[j + 1] = tmp;
            }
        }
    }

    return answer;
}