N = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for s in student:
    s -= B
    answer += 1
    if s > 0:
        answer += s // C
        if s % C != 0:
            answer += 1

print(answer)