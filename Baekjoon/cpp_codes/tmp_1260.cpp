#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

void fun(int st);

queue <int> q[10001];
vector <int> graph[10001];
int visited2[10001] = { 0, };

int main() {
	int n, m, v;
	int visited[10001] = { 0, };
	scanf("%d %d %d", &n, &m, &v);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	

	for (int i = 0; i < n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	fun(v);
	printf("\n");
	queue <int> q;

	q.push(v);
	visited[v] = 1;

	while (!q.empty()) {
		int cur_node = q.front();
		printf("%d ", cur_node);
		q.pop();

		for (int next : graph[cur_node]) {
			if (!visited[next]) {
				q.push(next);
				visited[next] = 1;
			}
		}
	}

	return 0;
}

void fun(int cur_node) {
	
	printf("%d ", cur_node);
	visited2[cur_node] = 1;

	for (int next : graph[cur_node]) {
		if (visited2[next] == 0)
			fun(next);
	}

	return;
}