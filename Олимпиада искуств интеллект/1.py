import time
import random
import matplotlib.pyplot as plt
import numpy as np


# Реализации алгоритмов сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Функция для измерения времени выполнения
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time


# Основная функция
def main():
    # Параметры эксперимента
    min_size = 100
    max_size = 3000
    step = 50
    sizes = list(range(min_size, max_size + 1, step))

    # Алгоритмы для тестирования
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Quick Sort': quick_sort,
        'Merge Sort': merge_sort
    }

    # Результаты
    results = {name: [] for name in algorithms.keys()}

    # Проводим эксперименты
    print("Запуск экспериментов...")
    for size in sizes:
        # Генерируем случайный массив
        arr = [random.randint(1, 5000) for _ in range(size)]

        for name, func in algorithms.items():
            time_taken = measure_time(func, arr)
            results[name].append(time_taken)
            print(f"Размер: {size}, Алгоритм: {name}, Время: {time_taken:.4f} сек")

    # Построение графиков
    plt.figure(figsize=(12, 8))

    for name, times in results.items():
        plt.plot(sizes, times, label=name, linewidth=2)

    plt.xlabel('Размер массива (элементов)')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение скорости работы алгоритмов сортировки')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.yscale('log')  # Логарифмическая шкала для лучшего отображения

    # Сохраняем график
    plt.savefig('sorting_algorithms_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Вывод статистики
    print("\nСтатистика:")
    for name, times in results.items():
        avg_time = np.mean(times)
        max_time = np.max(times)
        print(f"{name}: среднее время = {avg_time:.4f} сек, максимальное = {max_time:.4f} сек")
if __name__ == "__main__":
    main()