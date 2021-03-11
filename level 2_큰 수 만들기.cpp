#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    vector <int> v;
    int temp = k;

    for (int i = 0; i < number.size(); i++) {
        int cur = number[i]; //현재 넣고 싶은 숫자

        if ((temp == 0) || (v.empty())) {  //더 빼지 않아야 할 때
            v.push_back(cur);
            continue;
        }
        int size = v.size();
        for (int j = 0; j < size; j++) {  //size 자리에 바로 v.size()를 넣으면 원하는 만큼 반복문을 돌지않음
            if ((v.back() < cur) && (temp > 0) && (!v.empty())) {
                v.pop_back();
                temp--;
            }
            else {
                break;
            }
        }
        v.push_back(cur);
    }

    for (int i = 0; i < number.size() - k; i++) {
        answer += v[i];
    }

    return answer;
}