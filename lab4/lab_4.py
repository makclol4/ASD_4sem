import sys

def readGraph(filename):
    graph = []
    with open(filename) as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            graph.append(row)
    return graph

filename = "graph.txt"
graph = readGraph(filename)

def dfs(graph, visited, start, component):
    visited[start] = True
    component.append(start)
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)

def findComponents(graph):
    visited = [False] * len(graph)
    components = []
    for i in range(len(graph)):
        if not visited[i]:
            component = []
            dfs(graph, visited, i, component)
            components.append(component)
    return components

components = findComponents(graph)
with open('output.txt', 'w') as f:
    f.write(f"Number of components: {len(components)}\n\n")
    for i, component in enumerate(components):
        f.write(f"Component {i+1}: {component}\n")
    
