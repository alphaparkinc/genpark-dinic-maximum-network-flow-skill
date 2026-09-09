from collections import deque

class DinicMaxFlow:
    """Dinic's blocking flow algorithm for maximum network flow."""
    def __init__(self, num_vertices: int):
        self.n = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.level = [-1] * num_vertices

    def add_edge(self, u: int, v: int, capacity: float):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def _bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def _dfs(self, u: int, t: int, push: float, ptr: list[int]) -> float:
        if u == t or push == 0:
            return push
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                tr = self._dfs(v, t, min(push, cap), ptr)
                if tr > 0:
                    self.graph[u][i][1] -= tr
                    self.graph[v][rev][1] += tr
                    return tr
        return 0.0

    def compute_max_flow(self, source: int, sink: int) -> dict:
        total_flow = 0.0
        while self._bfs(source, sink):
            ptr = [0] * self.n
            while True:
                pushed = self._dfs(source, sink, float('inf'), ptr)
                if pushed == 0:
                    break
                total_flow += pushed

        return {
            "source": source,
            "sink": sink,
            "max_flow": total_flow
        }
