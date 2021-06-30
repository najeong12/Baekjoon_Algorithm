import copy
import sys
input = sys.stdin.readline

X = 0
Y = 1
DIRECTION = 2
LIVE = 3
DEAD = 0

total_time = 0
N, M, K = map(int, input().split())
count_shark = M
shark_info = [[-1, -1, -1, 1] for _ in range(M)]
shark_smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark_prio = [[None for _ in range(4)] for _ in range(M)]
next_shark_info = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어의 [x좌표, y좌표, 방향, 생사여부]를 저장하고 있는 배열 입력받기
def get_shark_info():
    global N, M, shark_info, LIVE
    for i in range(N):
        _map = list(map(int, input().split()))
        for j in range(N):
            if _map[j] != 0:
                shark_info[_map[j]-1][X] = i
                shark_info[_map[j]-1][Y] = j

    _dir = list(map(int, input().split()))
    for i in range(M):
        shark_info[i][DIRECTION] = _dir[i]-1

# 상어의 우선순위를 저장하는 배열 입력받기
def get_shark_prio():
    global N, M, shark_prio
    for i in range(M):
        for j in range(4):
            _dir = list(map(int, input().split()))
            shark_prio[i][j] = [_dir[0]-1, _dir[1]-1, _dir[2]-1, _dir[3]-1]

# 현재위치에 상어의 냄새 뿌리기
def put_smell():
    global shark_info, shark_smell, K
    for i in range(M):
        _x = shark_info[i][X]
        _y = shark_info[i][Y]
        if shark_info[i][LIVE] != DEAD:
            shark_smell[_x][_y][0] = i
            shark_smell[_x][_y][1] = K

# 해당 번호의 상어가 살아있으면 상어번호 반환
def if_exist(shark_info, x, y):
    global M
    for i in range(M):
        if (shark_info[i][0] == x) and (shark_info[i][1] == y) and (shark_info[i][LIVE] != DEAD):
            return i
    return -1

# 모든 상어 움직이기
def move_shark(shark_num, shark_x, shark_y, shark_dir): # 움직일 상어의 현재위치
    global N, M, shark_info, shark_smell, shark_prio, dx, dy, LIVE, count_shark, next_shark_info
    flag1 = 0
    flag2 = 0
    # 빈 칸이 있을 때
    for i in range(4):
        _dir = shark_prio[shark_num][shark_dir][i]
        nx = shark_x + dx[_dir]
        ny = shark_y + dy[_dir]
        # 경계내에 있고 냄새가 없으면
        if (0 <= nx < N) and (0 <= ny < N) and (shark_smell[nx][ny][1] == 0):
            flag1 = 1
            exist = if_exist(next_shark_info, nx, ny)
            # 상어가 없으면 그냥 넣어주기
            if exist == -1:
                next_shark_info[shark_num][X] = nx
                next_shark_info[shark_num][Y] = ny
                next_shark_info[shark_num][DIRECTION] = _dir
                next_shark_info[shark_num][LIVE] = 1
                break
            # 상어가 있으면 작은거 넣어주기
            else:
                count_shark -= 1
                if exist > shark_num:
                    next_shark_info[shark_num][X] = nx
                    next_shark_info[shark_num][Y] = ny
                    next_shark_info[shark_num][DIRECTION] = _dir
                    next_shark_info[shark_num][LIVE] = 1
                    next_shark_info[exist][LIVE] = DEAD
                    break
                else:
                    next_shark_info[shark_num][X] = nx
                    next_shark_info[shark_num][Y] = ny
                    next_shark_info[shark_num][DIRECTION] = _dir
                    next_shark_info[shark_num][LIVE] = 0
                    break

    # 모두 냄새로 막혔을 때 자신의 냄새로 이동
    if flag1 == 0:
        for i in range(4):
            _dir = shark_prio[shark_num][shark_dir][i]
            nx = shark_x + dx[_dir]
            ny = shark_y + dy[_dir]
            if (0 <= nx < N) and (0 <= ny < N) and (shark_smell[nx][ny][0] == shark_num) and (shark_smell[nx][ny][1] > 0):
                flag2 = 1
                exist = if_exist(next_shark_info, nx, ny)
                # 상어가 없으면 그냥 넣어주기
                if exist == -1:
                    next_shark_info[shark_num][X] = nx
                    next_shark_info[shark_num][Y] = ny
                    next_shark_info[shark_num][DIRECTION] = _dir
                    next_shark_info[shark_num][LIVE] = 1
                    break
                # 상어가 있으면 작은거 넣어주기
                else:
                    count_shark -= 1
                    if exist > shark_num:
                        next_shark_info[shark_num][X] = nx
                        next_shark_info[shark_num][Y] = ny
                        next_shark_info[shark_num][DIRECTION] = _dir
                        next_shark_info[shark_num][LIVE] = 1
                        next_shark_info[exist][LIVE] = DEAD
                        break
                    else:
                        next_shark_info[shark_num][X] = nx
                        next_shark_info[shark_num][Y] = ny
                        next_shark_info[shark_num][DIRECTION] = _dir
                        next_shark_info[shark_num][LIVE] = 0
                        break
    # 우선순위 따라 이동
    if flag2 == 0 and flag1 == 0:
        for i in range(4):
            _dir = shark_prio[shark_num][shark_dir][0]
            nx = shark_x + dx[_dir]
            ny = shark_y + dy[_dir]
            if (0 <= nx < N) and (0 <= ny < N):
                # 상어가 없으면 그냥 넣어주기
                exist = if_exist(next_shark_info, nx, ny)
                if exist == -1:
                    next_shark_info[shark_num][X] = nx
                    next_shark_info[shark_num][Y] = ny
                    next_shark_info[shark_num][DIRECTION] = _dir
                    next_shark_info[shark_num][LIVE] = 1
                    break
                # 상어가 있으면 작은거 넣어주기
                else:
                    count_shark -= 1
                    if exist > shark_num:
                        next_shark_info[shark_num][X] = nx
                        next_shark_info[shark_num][Y] = ny
                        next_shark_info[shark_num][DIRECTION] = _dir
                        next_shark_info[shark_num][LIVE] = 1
                        next_shark_info[exist][LIVE] = DEAD
                        break
                    else:
                        next_shark_info[shark_num][X] = nx
                        next_shark_info[shark_num][Y] = ny
                        next_shark_info[shark_num][DIRECTION] = _dir
                        next_shark_info[shark_num][LIVE] = 0
                        break

# 모든 냄새의 유지 시간 1 줄이기
def decrease_smell():
    global N, shark_smell
    for i in range(N):
        for j in range(N):
            if shark_smell[i][j][1] == 1:
                shark_smell[i][j][1] = 0
                shark_smell[i][j][0] = 0
            elif shark_smell[i][j][1] > 1:
                shark_smell[i][j][1] = shark_smell[i][j][1] - 1

get_shark_info()
get_shark_prio()

while count_shark > 1:  # 1번 상어만 남을 때까지
    total_time += 1
    if total_time == 1000:
        total_time = -1
        break
    decrease_smell()
    put_smell()
    next_shark_info.clear()
    next_shark_info = copy.deepcopy(shark_info)
    for i in range(M):
        next_shark_info[i][0] = -1
        next_shark_info[i][1] = -1
    for i in range(M):
        if shark_info[i][LIVE] != DEAD:
            move_shark(i, shark_info[i][X], shark_info[i][Y], shark_info[i][DIRECTION])
    shark_info.clear()
    shark_info = copy.deepcopy(next_shark_info)

print(total_time)