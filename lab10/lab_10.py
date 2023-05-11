def find_euler_cycle(adj_matrix):
    n = len(adj_matrix)
    degrees = [sum(adj_matrix[i]) for i in range(n)]
    odds = [i for i in range(n) if degrees[i] % 2 != 0]
    # проверяем условие эйлеровости
    if len(odds) != 0:
        return False
    # ищем эйлеров цикл
    stack = [0]
    cycle = []
    while len(stack) > 0:
        u = stack[-1]
        if degrees[u] > 0:
            v = -1
            for i in range(n):
                if adj_matrix[u][i] == 1:
                    degrees[u] -= 1
                    degrees[i] -= 1
                    adj_matrix[u][i] = 0
                    adj_matrix[i][u] = 0
                    v = i
                    stack.append(v)
                    break
            if v == -1:
                return False
        else:
            cycle.append(stack.pop())
    return True

# читаем матрицу смежности из input.txt
with open('input.txt', 'r') as f:
    n = int(f.readline())
    adj_matrix = [[int(x) for x in f.readline().split()] for i in range(n)]

# ищем эйлеров цикл
result = find_euler_cycle(adj_matrix)

# записываем "Yes" или "No" в output.txt
with open('output.txt', 'w') as f:
    f.write("Yes" if result else "No")