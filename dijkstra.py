import sys


def dijkstra(G, start):
    # U = list(G.keys())  # unvisited nodes

    U = set()  # unvisited nodes
    for k in G.keys():
        U.add(k)
        for p in G[k].keys():
            U.add(p)

    shortest_path = {}
    previous_nodes = {}

    for node in U:
        shortest_path[node] = sys.maxsize

    shortest_path[start] = 0

    while U:
        current_min_node = None
        for node in U:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        for neighbor, dist in G[current_min_node].items():
            # print(neighbor, dist)
            dist_tmp = shortest_path[current_min_node] + dist
            if dist_tmp < shortest_path[neighbor]:
                shortest_path[neighbor] = dist_tmp
                previous_nodes[neighbor] = current_min_node

        U.remove(current_min_node)

    return previous_nodes, shortest_path


if __name__ == "__main__":
    G = {
        "a": {"b": 85, "c": 10, "d": 19, "e": 32},
        "b": {"c": 78, "d": 88, "e": 28},
        "c": {"d": 28, "e": 39},
        "d": {"e": 11},
        "e": {}
    }
    print(dijkstra(G, "a"))
