N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))

house.sort()
start = 1
end = house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    position = house[0]

    for i in range(1, len(house)):
        if position + mid <= house[i]:
            count += 1
            position = house[i]

    if count < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)