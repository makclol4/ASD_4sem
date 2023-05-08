
def read_graph(filename):
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(map(int, line.strip().split())))

    return matrix


def dfs(graph, visited, start, component):
    # Обход в глубину для поиска сильно связанных компонент
    visited[start] = True
    component.append(start)
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)


def find_scc(graph):
    # Поиск всех сильно связанных компонент
    n = len(graph)
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i, order)
    transposed_graph = [[graph[j][i] for j in range(n)] for i in range(n)]
    visited = [False] * n
    scc_list = []
    for i in reversed(order):
        if not visited[i]:
            scc = []
            dfs(transposed_graph, visited, i, scc)
            scc_list.append(scc)
    return scc_list

input_file = "input_graph.txt"

    # Чтение графа из входного файла
graph = read_graph(input_file)

    # Поиск сильно связанных компонент
scc = find_scc(graph)

    # Запись результата в итоговый файл
with open('scc_result.txt', 'w') as f:
    f.write(f"Number of SCCs: {len(scc)}\n")
    for i, component in enumerate(scc):
        f.write(f"SCC {i+1}: {component}\n")