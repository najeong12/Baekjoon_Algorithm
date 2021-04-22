N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
member = []
for i in range(N):
    member.append(i)

def my_combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in my_combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

team = []
for comb in my_combinations(member, N//2):
    tmp = 0
    for comb2 in my_combinations(comb, 2):
        tmp += power[comb2[0]][comb2[1]] + power[comb2[1]][comb2[0]]
    team.append(tmp)


answer = abs(team[0] - team[-1])
for i in range(len(team)//2):
    answer = min(answer, abs(team[i] - team[-i-1]))

print(answer)