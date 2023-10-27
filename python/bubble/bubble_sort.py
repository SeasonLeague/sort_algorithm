def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# You can use this function to sort a list of numbers.
my_list = [64, 34, 25, 12, 22, 11, 90, 91, 92]
bubble_sort(my_list)
print("Sorted list:", my_list)
