
input_file = 'input.txt'
output_file = 'output.txt'

def bellman_ford(graph, start_vertex):
    # инициализация списков
    distances = [float('inf')] * len(graph)
    predecessors = [None] * len(graph)

    distances[start_vertex] = 0  # расстояние до стартовой вершины равно 0

    # проходимся по всем ребрам графа
    for _ in range(len(graph)-1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u

    return distances, predecessors


# считываем граф из файла
with open(input_file, 'r') as f:
    graph = []
    for line in f:
        graph.append(list(map(int, line.strip().split())))

# запускаем алгоритм Беллмана-Форда
start_vertex = 0
distances, predecessors = bellman_ford(graph, start_vertex)



result = ''
for i in range(len(distances)):
    result += f'{i}: {distances[i]}\n'

with open(output_file, 'w') as f:
    f.write(result)

