str1, str2 = map(str, input().split())
MIN = 100


def function(i):
    global str1, str2
    answer = 0
    for x in range(len(str1)):
        if str1[x] != str2[i+x]:
            answer += 1
    return answer

for i in range(len(str2) - len(str1) + 1):
    MIN = min(MIN, function(i))

print(MIN) 