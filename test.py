if __name__ == '__main__':
    N, K = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0 for _ in range(N)]

    print(N, K)
    print(belt)