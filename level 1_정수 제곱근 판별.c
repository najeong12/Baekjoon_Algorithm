#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long solution(long long n) {
    long long answer = 0;

    if ((int)sqrt(n) * sqrt(n) == n)
        answer = (sqrt(n) + 1) * (sqrt(n) + 1);
    else
        answer = -1;

    return answer;
}