
filename = "input.txt"

# функция для считывания строки из файла
def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

# функция для реализации алгоритма Бойера-Мура
def boyer_moore_search(text, pattern):
    # определяем длину строки и образца
    n, m = len(text), len(pattern)
    # если длина образца равна нулю, то его нет в тексте
    if m == 0:
        return 0
    # задаем таблицу смещений
    skip = {char: m for char in pattern}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    # начинаем поиск с конца строки
    i = m - 1
    while i < n:
        # проверяем совпадение символов с конца строки и образца
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        # считаем необходимое смещение
        i += max(skip.get(text[i], m), m - j)
    # если образец не найден, возвращаем -1
    return -1

# основная функция программы
def main():
    # считываем строку из файла
    text = read_file(filename)
    # вводим образец
    pattern = input("Введите образец для поиска: ")
    # ищем образец в строке
    index = boyer_moore_search(text, pattern)
    if index == -1:
        print("Образец не найден")
    else:
        print(f"Образец найден в позиции {index}")

# вызываем основную функцию
if __name__ == "__main__":
    main()