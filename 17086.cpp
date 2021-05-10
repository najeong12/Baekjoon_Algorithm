#include <iostream>
#include <vector>
#include <queue>

#define my_max(a, b) (((a)>(b))?(a):(b))

int N, M, MAX;
int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};
std::vector<std::vector<int> > shark;
std::vector<std::vector<int> > shark2;

struct point{
    int x;
    int y;
};

void input_faster()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

void input()
{
    std::cin >> N >> M;
    shark.resize(N+1, std::vector<int>(M+1,0));
    for(int i = 0 ; i < N ; i ++){
        for (int j = 0 ; j < M ; j ++){
            std::cin >> shark[i][j];
        }
    }
}

int bfs(int x, int y){
    int nx, ny, _safe;
    point _arr;
    std::queue <int> safe;
    std::queue <point> arr;
    shark2 = shark;
    if (shark2[x][y] == 1)
        return 0;
    safe.push(0);
    point p;
    p.x = x;
    p.y = y;
    arr.push(p);
    shark2[x][y] = 2;
    while (safe.size() > 0)
    {
        _safe = safe.front();
        safe.pop();
        _arr = arr.front();
        arr.pop();
        for(int k = 0 ; k < 8 ; k++){    
            nx = _arr.x + dx[k];
            ny = _arr.y + dy[k];
            if ((0 <= nx) && (nx < N) && (0 <= ny) && (ny < M) && shark2[nx][ny] != 2){
                if (shark2[nx][ny] == 1){
                    return _safe + 1;
                }
                else{
                    point p2;
                    p2.x = nx;
                    p2.y = ny;
                    arr.push(p2);
                    safe.push(_safe+1);
                    shark2[nx][ny] = 2;
                }
            }
        }
    }
    return my_max(N, M);
}

void solve()
{
    MAX = 0;
    for (int i = 0 ; i < N ; i++)
        for (int j = 0 ; j < M ; j++)
         MAX = my_max(MAX, bfs(i, j));
}

void print_val()
{
  std::cout << MAX;
}

int main()
{
	input_faster();
	input();
	solve();
	print_val();
	return (0);
}
