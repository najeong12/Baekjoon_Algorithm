import copy

def shortest_time(start, end, taxi_map):
    print("taxi_map= ", taxi_map)
    taxi_tmp = copy.deepcopy(taxi_map)
    taxi_tmp[start[0]-1][start[1]-1] = 1
    print("taxi_map= ", taxi_tmp)
    tmp1 = [[start[0]-1, start[1]-1]]
    print("tmp1 = ",tmp1)
    tmp_len = [0]
    result = [] # 도착지의 x, y, len을 저장하는 배열
    while True:
        _len = tmp_len[0] + 1 # 출발지와 현재위치까지의 거리
        tmp_len.remove(tmp_len[0])
        x = tmp1[0][0]
        y = tmp1[0][1]
        print(x, y)
        print("tmp1[0] = ", tmp1[0])
        tmp1.remove(tmp1[0])
        print(tmp1)
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            print("nx, ny = ", nx, ny)
            if (0 <= nx < N) and (0 <= ny < N) and (taxi_tmp[nx][ny] == 0):
                print("---")
                for t in taxi_tmp:
                    print(t)
                taxi_tmp[nx][ny] = 1
                print("-")
                for t in taxi_tmp:
                    print(t)
                print(tmp1)
                tmp1.append([nx, ny])
                print(tmp1)
                print(tmp_len)
                tmp_len.append(_len)
                print(tmp_len)
                print("---")
                print("end = ",[end[0]-1, end[1]-1])
                if tmp1[-1] == [end[0]-1, end[1]-1]:
                    print("222222222")
                    result.append(nx)
                    result.append(ny)
                    break

        if len(tmp_len) == 0:
            break
        if tmp1[-1] == [end[0]-1, end[1]-1]:
            break

    if len(tmp_len) == 0:
        result.append(-1)
    else:
        result.append(tmp_len[-1])

    print("result=", result)
    return result

def shortest_person(person, taxi, taxi_map):
    info1 = shortest_time(taxi, person[0], taxi_map)
    if info1[0] == -1:
        return info1

    for i in range(1, len(person)):
        info2 = shortest_time(taxi, person[i], taxi_map)
        if info1[2] > info2[2]:
            info1 = info2
        elif info1[2] == info2[2]:
            if info1[0] > info2[0]:
                info1 = info2
            elif info1[0] == info2[0]:
                if info1[1] > info2[1]:
                    info1 = info2

    return info1

if __name__ == '__main__':
    person = []
    dest = []
    dir =[[-1, 0],[0, 1],[1, 0],[0, -1]]

    ## 입력받기
    N, M, fuel = map(int, input().split())
    taxi_map = [list(map(int, input().split())) for _ in range(N)]
    taxi = list(map(int, input().split()))
    for _ in range(M):
        tmp = list(map(int, input().split()))
        person.append([tmp[0], tmp[1]])
        dest.append([tmp[2], tmp[3]])

    person2 = copy.deepcopy(person)

    ## 가장 가까운 승객 찾기
    for i in range(M):
        passanger_info = shortest_person(person, taxi, taxi_map)
        if passanger_info[0] == -1:
            fuel = -1
            break
        print(passanger_info)
        if fuel < passanger_info[2]: fuel = -1; break
        fuel -= passanger_info[2]
        print("\nfuel = ", fuel)

        now_person = [passanger_info[0], passanger_info[1]] # 현재 태우고 있는 승객의 위치
        taxi = [now_person[0]+1, now_person[1]+1]
        print("--------------taxi=", taxi)
        idx = person2.index([now_person[0]+1, now_person[1]+1])
        move_len = shortest_time(taxi, dest[idx], taxi_map)[2]
        if fuel < move_len: fuel = -1; break
        fuel += move_len
        print("\nmove_len = ", move_len)
        person.remove([now_person[0]+1, now_person[1]+1])
        print("last fuel = ", fuel)
        taxi = dest[idx]
        print("--------------taxi=", taxi)

    print(fuel)