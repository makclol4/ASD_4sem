# -*- coding: utf-8 -*-


# определяем структуру графа, используя словарь
graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
        }

# определяем количество цветов, используемых в раскраске
num_colors = 3

# инициализируем список цветов, присваивая каждой вершине пустой цвет
vertex_colors = {}

# определяем функцию для проверки, можно ли назначить этот цвет вершине на основе цветов ее соседей
def is_color_valid(vertex, color):
    # проходим по списку смежных вершин
    for neighbor in graph[vertex]:
        # если соседняя вершина уже имеет такой цвет, результат ложный
        if vertex_colors.get(neighbor) == color:
            return False
    # если все соседи имеют разные цвета, результат истинный
    return True

# жадный алгоритм раскраски графа
for vertex in graph:
    # проходим по всем цветам и пытаемся найти минимальный доступный цвет
    for color in range(num_colors):
        if is_color_valid(vertex, color):
            vertex_colors[vertex] = color
            break

# выводим итоговую раскраску вершин графа
for vertex, color in vertex_colors.items():
    print(f"{vertex}: {color}")