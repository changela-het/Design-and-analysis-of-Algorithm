"""
Program 8: Implementation of Graph and Searching (DFS and BFS)
"""

from collections import deque, defaultdict


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)
        else:
            self.adj.setdefault(v, self.adj[v])  # ensure v exists as a node

    # ---------------- Depth First Search ----------------
    def dfs(self, start):
        visited = set()
        order = []
        self._dfs_helper(start, visited, order)
        return order

    def _dfs_helper(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, order)

    def dfs_iterative(self, start):
        visited = set()
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # push neighbors in reverse so traversal order matches recursive DFS
                for neighbor in reversed(self.adj[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    # ---------------- Breadth First Search ----------------
    def bfs(self, start):
        visited = {start}
        order = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


def main():
    g = Graph(directed=False)
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('C', 'D'),
        ('D', 'E'), ('E', 'F'),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Graph edges:", edges)
    print("\nDFS (recursive) from A:", g.dfs('A'))
    print("DFS (iterative) from A:", g.dfs_iterative('A'))
    print("BFS from A:", g.bfs('A'))


if __name__ == "__main__":
    main()
