with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    matrix = [[int(j) for j in f.readline().strip().split()] for i in range(n)]

edges = []

visited = [0]

available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and (i in visited) != (j in visited)]

for i in range(n-1):

    e = min(available_edges, key=lambda x: x[2])

    edges.append(e)

    new_vertex = e[0] if e[1] in visited else e[1]
    visited.append(new_vertex)

    available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and ((i in visited) != (j in visited)) and ((i, j) not in edges) and ((j, i) not in edges)]

with open("output.txt", "w") as f:
    for e in edges:
        f.write("{} {} {}\n".format(e[0]+1, e[1]+1, e[2]))