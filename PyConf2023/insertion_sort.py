"""
Insertion Sort builds the sorted portion of the list one element at a time by repeatedly taking
the next unsorted element and inserting it into its correct position.
It is more efficient than Bubble and Selection Sort with a time complexity of O(n^2) in the worst case.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
