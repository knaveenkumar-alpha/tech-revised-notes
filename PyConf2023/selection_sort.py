"""
Selection Sort repeatedly selects the minimum element from the unsorted portion of the list and
moves it to the beginning.
It also has a time complexity of O(n^2) in the worst and average cases.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx],  arr[i]


my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
