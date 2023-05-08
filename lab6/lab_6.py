with open("input.txt", "r") as f:
    n = int(f.readline().strip()) # число вершин
    matrix = [[int(j) for j in f.readline().strip().split()] for i in range(n)]

# инициализация списка ребер
edges = []
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] != 0:
            edges.append((i, j, matrix[i][j]))

edges.sort(key=lambda e: e[2])

result = []

sets = [{i} for i in range(n)]

def find_set(vertex):
    for s in sets:
        if vertex in s:
            return s
    return None

for e in edges:
    u, v, w = e
    set1 = find_set(u)
    set2 = find_set(v)
    if set1 != set2:
        result.append(e)
        sets.remove(set1)
        sets.remove(set2)
        sets.append(set1.union(set2))


with open("output.txt", "w") as f:
    for e in result:
        f.write("{} {} {}\n".format(e[0]+1, e[1]+1, e[2]))