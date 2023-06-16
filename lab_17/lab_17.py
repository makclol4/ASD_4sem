
def distribute_items(num_items, num_boxes, max_items):
    """
    Функция для распределения предметов по ящикам.
    
    :param num_items: количество предметов
    :param num_boxes: количество ящиков
    :param max_items: максимальное количество предметов в одном ящике
    :return: список, соответствующий распределению предметов по ящикам или None 
    в случае невозможности распределения
    """
    # Создаем список, соответствующий распределению предметов по ящикам
    box_items = [0] * num_boxes

    # Рекурсивно распределяем предметы по ящикам
    if not distribute_recursive(num_items, num_boxes, max_items, box_items, 0):
        # Если распределение невозможно, возвращаем None
        return None

    return box_items

"""
Функция `distribute_recursive` принимает пять параметров: оставшееся количество
предметов для распределения, количество ящиков, максимальное количество предметов
в одном ящике, список, соответствующий распределению предметов по ящикам, 
и текущий ящик, в который добавляются предметы. Она рекурсивно распределяет 
предметы по ящикам, пытаясь добавлять их в текущий ящик или переходить к следующему, 
если текущий уже содержит максимальное количество предметов.
"""

def distribute_recursive(num_items, num_boxes, max_items, box_items, current_box):
    """
    Функция для рекурсивного распределения предметов по ящикам.

    :param num_items: оставшееся количество предметов для распределения
    :param num_boxes: количество ящиков
    :param max_items: максимальное количество предметов в одном ящике
    :param box_items: список, соответствующий распределению предметов по ящикам
    :param current_box: текущий ящик, в который добавляются предметы
    :return: True, если распределение возможно, иначе False
    """
    # Если все предметы распределены, возвращаем True
    if num_items == 0:
        return True

    if current_box >= num_boxes:
        return False
    # Если текущий ящик уже содержит максимальное количество предметов, пытаемся распределить
    #предметы в следующем ящике
    if box_items[current_box] == max_items:
        return distribute_recursive(num_items, num_boxes, max_items, box_items, current_box + 1)

    # Распределяем предметы в текущий ящик
    for i in range(min(num_items, max_items - box_items[current_box]) + 1):
        box_items[current_box] += i
        if distribute_recursive(num_items - i, num_boxes, max_items, box_items, current_box + 1):
            return True
        box_items[current_box] -= i

    # Если распределение невозможно, возвращаем False
    return False

num_items = 10
num_boxes = 3
max_items = 5

box_items = distribute_items(num_items, num_boxes, max_items)
if box_items is not None:
    print(f'Предметы распределены по ящикам: {box_items}')
else:
    print('Распределение невозможно')




