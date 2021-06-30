#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int sum_fn(int n) {
    int answer = 0;
    while (n > 0) {
        answer += n % 10;
        n /= 10;
    }
    return answer;
}

bool solution(int x) {
    bool answer = true;
    if (x % sum_fn(x) != 0) {
        answer = false;
    }

    return answer;
}