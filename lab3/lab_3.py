with open('graph.txt', 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]

n = len(matrix)

visited = [False] * n

components = []

def bfs(start_node, graph, visited, component):
    # Очередь для обхода
    queue = [start_node]
    visited[start_node] = True

    while queue:
        node = queue.pop(0)
        component.append(node)

        # Перебор смежных вершин
        for i in range(n):
            if graph[node][i] and not visited[i]:
                visited[i] = True
                queue.append(i)


# Обход графа
for i in range(n):
    if not visited[i]:
        component = []
        bfs(i, matrix, visited, component)
        components.append(component)



with open('output.txt', 'w') as file:
    file.write(f'Количество компонент связности: {len(components)}\n\n')
    for i, component in enumerate(components):
        file.write(f'Компонента связности {i + 1}: {component}\n')
