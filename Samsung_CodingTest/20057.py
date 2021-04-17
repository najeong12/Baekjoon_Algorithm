dr=[]
dc=[]
sand=[]

def fill_sand():
    for i in range(N): sand.append(list(map(int, input().split())))

def fill_dr_dc(N):
    for i in range(1, N, 2):
        for j in range(i): dr.append(0); dc.append(-1)
        for j in range(i): dr.append(1); dc.append(0)
        for j in range(i+1): dr.append(0); dc.append(1)
        for j in range(i+1): dr.append(-1); dc.append(0)
    for i in range(N): dr.append(0); dc.append(-1)

def move_sand1(next_sand, _r, _c, outer_sand, dr, dc):
    sum_sand = 0
    if ((0 <= (_r + 2*dr) < N) and (0 <= (_c + 2*dc) < N)):  sand[_r + 2*dr][_c +2*dc] += int(next_sand * (0.05))
    else: outer_sand += int(next_sand * (0.05));
    sum_sand += int(next_sand * (0.05))
    if ((0 <= (_r + dr - 1) < N) and (0 <= (_c +dc) < N)):  sand[_r + dr - 1][_c + dc] += int(next_sand * (0.1))
    else: outer_sand += int(next_sand * (0.1));
    sum_sand += int(next_sand * (0.1))
    if ((0 <= (_r + dr + 1) < N) and (0 <= (_c + dc) < N)): sand[_r + dr + 1][_c + dc] += int(next_sand * (0.1))
    else: outer_sand += int(next_sand * (0.1));
    sum_sand += int(next_sand * (0.1))
    if ((0 <= (_r - 1) < N) and (0 <= (_c + 0) < N)):  sand[_r - 1][_c + 0] += int(next_sand * (0.07))
    else: outer_sand += int(next_sand * (0.07));
    sum_sand += int(next_sand * (0.07))
    if ((0 <= (_r + 1) < N) and (0 <= (_c + 0) < N)):  sand[_r + 1][_c + 0] += int(next_sand * (0.07))
    else: outer_sand += int(next_sand * (0.07));
    sum_sand += int(next_sand * (0.07))
    if ((0 <= (_r + 2) < N) and (0 <= (_c + 0) < N)):  sand[_r + 2][_c + 0] += int(next_sand * (0.02))
    else: outer_sand += int(next_sand * (0.02));
    sum_sand += int(next_sand * (0.02))
    if ((0 <= (_r - 2) < N) and (0 <= (_c + 0) < N)):  sand[_r - 2][_c + 0] += int(next_sand * (0.02))
    else: outer_sand += int(next_sand * (0.02));
    sum_sand += int(next_sand * (0.02))
    if ((0 <= (_r -dr + 1) < N) and (0 <= (_c - dc) < N)):  sand[_r -dr + 1][_c - dc] += int(next_sand * (0.01))
    else: outer_sand += int(next_sand * (0.01));
    sum_sand += int(next_sand * (0.01))
    if ((0 <= (_r -dr - 1) < N) and (0 <= (_c - dc) < N)):  sand[_r -dr - 1][_c - dc] += int(next_sand * (0.01))
    else: outer_sand += int(next_sand * (0.01));
    sum_sand += int(next_sand * (0.01))

    if ((0 <= (_r + dr) < N) and (0 <= (_c + dc) < N)):  sand[_r + dr][_c + dc] += (next_sand - sum_sand)
    else: outer_sand += (next_sand - sum_sand)

    return outer_sand

def move_sand2(next_sand, _r, _c, outer_sand, dr, dc):
    sum_sand = 0
    if ((0 <= (_r + 2*dr) < N) and (0 <= (_c + 2*dc) < N)):  sand[_r + 2*dr][_c +2*dc] += int(next_sand * (0.05))
    else: outer_sand += int(next_sand * (0.05));
    sum_sand += int(next_sand * (0.05))
    if ((0 <= (_r + dr) < N) and (0 <= (_c + dc - 1) < N)):  sand[_r + dr][_c + dc - 1] += int(next_sand * (0.1))
    else: outer_sand += int(next_sand * (0.1));
    sum_sand += int(next_sand * (0.1))
    if ((0 <= (_r + dr) < N) and (0 <= (_c + dc + 1) < N )): sand[_r + dr][_c + dc + 1] += int(next_sand * (0.1))
    else: outer_sand += int(next_sand * (0.1));
    sum_sand += int(next_sand * (0.1))
    if ((0 <= (_r + 0) < N) and (0 <= (_c + 1) < N)):  sand[_r + 0][_c + 1] += int(next_sand * (0.07))
    else: outer_sand += int(next_sand * (0.07));
    sum_sand += int(next_sand * (0.07))
    if ((0 <= (_r + 0) < N) and (0 <= (_c - 1) < N)):  sand[_r + 0][_c - 1] += int(next_sand * (0.07))
    else: outer_sand += int(next_sand * (0.07));
    sum_sand += int(next_sand * (0.07))
    if ((0 <= (_r + 0) < N) and (0 <= (_c + 2) < N)):  sand[_r + 0][_c + 2] += int(next_sand * (0.02))
    else: outer_sand += int(next_sand * (0.02));
    sum_sand += int(next_sand * (0.02))
    if ((0 <= (_r + 0) < N) and (0 <= (_c - 2) < N)):  sand[_r + 0][_c - 2] += int(next_sand * (0.02))
    else: outer_sand += int(next_sand * (0.02));
    sum_sand += int(next_sand * (0.02))
    if ((0 <= (_r -dr) < N) and (0 <= (_c - dc + 1) < N)):  sand[_r -dr][_c - dc + 1] += int(next_sand * (0.01))
    else: outer_sand += int(next_sand * (0.01));
    sum_sand += int(next_sand * (0.01))
    if ((0 <= (_r -dr) < N) and (0 <= (_c - dc - 1) < N)):  sand[_r -dr][_c - dc - 1] += int(next_sand * (0.01))
    else: outer_sand += int(next_sand * (0.01));
    sum_sand += int(next_sand * (0.01))

    if ((0 <= (_r + dr) < N) and (0 <= (_c + dc) < N)):  sand[_r + dr][_c + dc] += (next_sand - sum_sand)
    else: outer_sand += (next_sand - sum_sand)

    return outer_sand

if __name__ == '__main__':
    N = int(input())
    outer_sand = 0
    fill_sand()
    fill_dr_dc(N)

    _r = (N//2) #가운데 칸의 인덱스
    _c = (N//2)
    for i in range(len(dr)):
        _r = _r + dr[i]; _c = _c + dc[i]
        next_sand = sand[_r][_c]
        if dr[i] == 0:
            outer_sand = move_sand1(next_sand, _r, _c, outer_sand, dr[i], dc[i])
        else:
            outer_sand = move_sand2(next_sand, _r, _c, outer_sand, dr[i], dc[i])
        sand[_r][_c] = 0

    print(outer_sand)