# -*- coding: utf-8 -*-

# Определим функцию, которая строит конечный автомат по строке-образцу
def build_automaton(pattern):
    alphabet = set(pattern) # создадим алфавит из символов, входящих в строку-образец
    automaton = [{ch: 0 for ch in alphabet} for _ in range(len(pattern) + 1)] # создадим конечный автомат с пустыми переходами
    for state in range(len(pattern) + 1): # заполним переходы по символам из алфавита
        for ch in alphabet:
            next_state = min(len(pattern), state + 1) # определим следующее состояние
            while next_state > 0 and pattern[:next_state] != pattern[state-next_state+1:state+1]:
                next_state -= 1 # корректируем следующее состояние, пока не найдем возможный префикс для перехода
            automaton[state][ch] = next_state # запишем следующее состояние в таблицу переходов
    return automaton



# Определим функцию, которая будет искать строку-образец в строке-тексте
def find_pattern(text, pattern):
    automaton = build_automaton(pattern) # построим конечный автомат по строке-образцу
    state = 0 # начинаем обработку из начального состояния автомата
    for i, ch in enumerate(text): # обрабатываем каждый символ из строки-текста
        if ch in automaton[state]: # проверяем, есть ли переход из текущего состояния по текущему символу
            state = automaton[state][ch] # переходим по автомату в следующее состояние
        else: # если перехода нет, возвращаемся на начальное состояние и продолжаем обработку с нового символа
            state = 0
        if state == len(pattern): # если достигнуто терминальное состояние автомата, значит строка-образец найдена
            return i - len(pattern) + 1 # возвращаем индекс первого символа найденного образца в строке-тексте
    return -1 # если образец не найден, возвращаем -1

# считываем строку из файла
input_file = 'input.txt'
with open(input_file) as f:
    text = f.readline().strip()

# ищем образец в строке
pattern = input('Введите строку-образец: ')
index = find_pattern(text, pattern)

# записываем результат в файл
output_file = 'output.txt'
with open(output_file, 'w') as f:
    if index != -1:
        f.write(f'Образец "{pattern}" найден в позиции {index} в строке-тексте: "{text}"')
    else:
        f.write(f'Образец "{pattern}" не найден в строке-тексте: "{text}"')