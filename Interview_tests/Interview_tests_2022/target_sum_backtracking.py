# Subset Sum Problem Using Backtracking
def subset_sum(arr, target):
    result = []

    def backtrack(start, current_sum, path):
        if current_sum == target:
            result.append(list(path))
            return
        for i in range(start, len(arr)):
            if current_sum + arr[i] <= target:
                path.append(arr[i])
                backtrack(i + 1, current_sum + arr[i], path)
                path.pop()

    arr.sort()
    backtrack(0, 0, [])
    return result


# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(arr, target))  # Output: [[3, 4, 2], [5, 4]]
