N = int(input())
number = list(map(int, input().split()))
operator = []
tmp = list(map(int, input().split()))
for i in range(4):
    if tmp[i] > 0:
        if i == 0:
            for j in range(tmp[i]):
                operator.append("+")
        if i == 1:
            for j in range(tmp[i]):
                operator.append("-")
        if i == 2:
            for j in range(tmp[i]):
                operator.append("*")
        if i == 3:
            for j in range(tmp[i]):
                operator.append("/")


def my_permutations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in my_permutations(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next

MIN = 1000000009
MAX = -1000000009
for perm in my_permutations(operator, N-1):
    num = number[0]
    for i in range(N-1):
        if perm[i] == '+':
            num += number[i+1]
        elif perm[i] == '-':
            num -= number[i+1]
        elif perm[i] == '*':
            num *= number[i+1]
        elif perm[i] == '/':
            if num < 0 and number[i+1] < 0:
                num = (-1 * num) // (-1 * number[i+1])
            elif (num < 0) and (number[i+1] > 0):
                num = -1 * ((-1 * num) // number[i + 1])
            elif (num > 0) and (number[i+1] < 0):
                num = -1 * (num // (-1 * number[i+1]))
            else:
                num = num // number[i+1]
    MIN = min(MIN, num)
    MAX = max(MAX, num)

print(MAX)
print(MIN)