"""
Quick Sort is a divide-and-conquer algorithm that selects a "pivot" element from the list and partitions
the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
It has an average-case time complexity of O(n log n) but can degrade to O(n^2) in the worst case.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
