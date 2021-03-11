#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = new_id;
    //1단계
    std::transform(answer.begin(), answer.end(), answer.begin(), ::tolower);

    //2단계
    for (int i = 0; i < answer.size(); i++) {
        char temp = answer[i];
        if (!(temp >= 'a' && temp <= 'z') && !(temp >= '0' && temp <= '9') && !(temp == '-') && !(temp == '_') && !(temp == '.')) {
            answer.erase(i, 1);
            i--;
        }
    }

    //3단계
    for (int i = 1; i < answer.size(); i++) {
        if (answer[i - 1] == '.' && answer[i] == '.') {
            answer.erase(i, 1);
            i--;
        }
    }

    //4단계
    if (answer[0] == '.')
        answer.erase(0, 1);
    if (answer[answer.size() - 1] == '.')
        answer.erase(answer.size() - 1, 1);

    //5단계
    if (answer.empty())
        answer = 'a';

    //6단계
    if (answer.size() >= 16)
        answer.erase(15, answer.size() - 15);

    //7단계
    if (answer.size() == 1) {
        answer += answer[answer.size() - 1];
        answer += answer[answer.size() - 1];
    }
    if (answer.size() == 2) {
        answer += answer[answer.size() - 1];
    }

    //4단계 한번더
    if (answer[0] == '.')
        answer.erase(0, 1);
    if (answer[answer.size() - 1] == '.')
        answer.erase(answer.size() - 1, 1);

    return answer;
}