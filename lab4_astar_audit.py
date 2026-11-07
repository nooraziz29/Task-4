import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def search(start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]
    costs = {start: 0}
    expanded = []

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if g > costs[node]:
            continue

        if node == goal:
            return path, g, expanded

        expanded.append(node)

        for next_node, edge_cost in graph[node]:
            new_cost = g + edge_cost

            if next_node not in costs or new_cost < costs[next_node]:
                costs[next_node] = new_cost
                new_f = new_cost + heuristic[next_node]

                heapq.heappush(
                    queue,
                    (new_f, new_cost, next_node, path + [next_node])
                )

    return None, float("inf"), expanded

# A* search
path, cost, expanded = search("S", "G", h)

print("A* Search")
print("Path:", path)
print("Cost:", cost)
print("Expanded nodes:", expanded)
print("Expansion count:", len(expanded))

# Uniform Cost Search
zero_h = {node: 0 for node in graph}
path, cost, expanded = search("S", "G", zero_h)

print("\nUniform Cost Search")
print("Path:", path)
print("Cost:", cost)
print("Expanded nodes:", expanded)
print("Expansion count:", len(expanded))

# Overestimated heuristic
new_h = h.copy()
new_h["C"] = 10

path, cost, expanded = search("S", "G", new_h)

print("\nOverestimated Heuristic")
print("Path:", path)
print("Cost:", cost)
print("Expanded nodes:", expanded)
print("Expansion count:", len(expanded))