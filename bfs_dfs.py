G = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}


def dfs(graph, node):
    stack = [node]
    visited = []
    # print("\nOrder of visited nodes by DFS: ", end=" ")
    while stack:
        s = stack.pop()

        if s not in visited:
            visited.append(s)
            # print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)


def bfs(graph, node):
    queue = [node]
    visited = [node]
    # print("\nOrder of visited nodes by BFS: ", end=" ")
    while queue:
        m = queue.pop(0)
        # print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


bfs(G, "5")
dfs(G, "5")
