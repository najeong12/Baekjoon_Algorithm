# T = int(input())
# for _ in range(T):
#     n = int(input())
#     note1 = set(map(int, input().split()))
#     m = int(input())
#     note2 = list(map(int, input().split()))
#     for num in note2:
#         if num in note1:
#             print(1)
#         else:
#             print(0)


def binary_search(start, end, num):
    global note1
    while start <= end:
        mid = (start + end) // 2
        if note1[mid] == num:
            return 1
        elif note1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

T = int(input())

for _ in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    for num in note2:
        print(binary_search(0, n-1, num))
