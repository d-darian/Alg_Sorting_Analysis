import time
import random

def insertion_sort(arr):
    start_time = time.time()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    end_time = time.time()
    return end_time - start_time

def selection_sort(arr):
    start_time = time.time()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.time()
    return end_time - start_time

def bubble_sort(arr):
    start_time = time.time()

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    return end_time - start_time

def merge_sort(arr):
    start_time = time.time()

    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort_helper(left_half)
            merge_sort_helper(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    merge_sort_helper(arr)

    end_time = time.time()
    return end_time - start_time

def heap_sort(arr):
    start_time = time.time()

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    end_time = time.time()
    return end_time - start_time

def quick_sort(arr):
    start_time = time.time()

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)

    end_time = time.time()
    return end_time - start_time

# Read input from file
with open("Input_10_1.txt", "r") as file:
    input_numbers = [int(num) for num in file.read().split()]

# Perform sorting and measure time
insertion_time = insertion_sort(input_numbers.copy())
print(f"Insertion Sort Time: {insertion_time:.6f} seconds")

selection_time = selection_sort(input_numbers.copy())
print(f"Selection Sort Time: {selection_time:.6f} seconds")

bubble_time = bubble_sort(input_numbers.copy())
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")

merge_time = merge_sort(input_numbers.copy())
print(f"Merge Sort Time: {merge_time:.6f} seconds")

heap_time = heap_sort(input_numbers.copy())
print(f"Heap Sort Time: {heap_time:.6f} seconds")

quick_time = quick_sort(input_numbers.copy())
print(f"Quick Sort Time: {quick_time:.6f} seconds")
