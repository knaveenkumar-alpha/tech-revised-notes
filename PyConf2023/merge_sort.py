"""
Merge Sort is also a divide-and-conquer algorithm that divides the list into smaller sub-lists,
sorts them, and then merges them to produce a sorted list.
It has a consistent time complexity of O(n log n) in all cases
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(my_list)
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
