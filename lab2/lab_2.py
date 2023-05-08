from queue import Queue

with open('graph.txt', 'r') as f:
    matrix = [list(map(int, line.strip().split())) for line in f]

# определяем стартовую вершину
start_node = 0

# создаем очередь
q = Queue()
q.put(start_node)

# создаем два массива
visited = [False] * len(matrix)
visited[start_node] = True
distances = [float('inf')] * len(matrix)
distances[start_node] = 0

# BFS 
while not q.empty():
    node = q.get()
    for neighbor, weight in enumerate(matrix[node]):
        if weight > 0 and not visited[neighbor]:
            visited[neighbor] = True
            q.put(neighbor)
            distances[neighbor] = distances[node] + weight


with open('result.txt', 'w') as f:
    for i, distance in enumerate(distances):
        f.write(f' Krotchaishi pyt do {i}: {distance}\n')