

# 조합
def combinations(arr, r):
    if r == 1:
        yield [arr[i]]
    else:
        for next in combinations(arr[i+1:], r-1):
            yield [arr[i]] + next

# 중복조합
def combinations(arr, r):
    if r == 1:
        yield [arr[i]]
    else:
        for next in combinations(arr[i:], r-1):
            yield [arr[i]] + next

# 순열
def permutaions(arr, r):
    if r == 1:
        yield [arr[i]]
    else:
        for next in permutations(arr[:i] + arr[i+1:], r-1):
            yield [arr[i]] + next