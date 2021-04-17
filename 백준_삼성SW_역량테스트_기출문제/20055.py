if __name__ == '__main__':
    N, K = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0 for _ in range(2*N)]

    cnt = 0  # 횟수를 저장할 변수
    up_idx = 0  # 올라가는 위치의 인덱스
    down_idx = N - 1  # 내려가는 위치의 인덱스

    while belt.count(0) < K:  # 내구도가 0인 벨트가 K개 이상이면 끝
        cnt += 1
        # 한칸씩 오른쪽으로 회전
        up_idx = (2 * N - 1) if (up_idx == 0) else (up_idx - 1)
        down_idx = (2 * N - 1) if (down_idx == 0) else (down_idx - 1)

        # 내려가는 위치에 있는 로봇내리기
        robot[down_idx] = 0

        # 로봇 오른쪽으로 한칸씩 이동(가능하면)
        for i in range(N):
            pos = down_idx-i if (down_idx-i >= 0) else (2*N + down_idx - i)
            next = 0 if (pos == (2 * N - 1)) else (pos + 1)
            if (robot[pos] == 1) and (robot[next] == 0) and (belt[next] > 0):
                belt[next] -= 1
                robot[pos] = 0
                robot[next] = 1

        # 내려가는 위치에 있는 로봇내리기
        robot[down_idx] = 0

        # 올라가는 위치에 로봇이 없다면 하나 올려주기
        if (robot[up_idx] == 0) and (belt[up_idx] > 0):
            robot[up_idx] = 1
            belt[up_idx] -= 1

    print(cnt)