def count_occurrences(arr, n, target):

    if n == 0:
        return 0

    count = count_occurrences(arr, n - 1, target)

    if arr[n - 1] == target:
        count += 1

    return count


arr = [1, 2, 2, 3, 2, 4]

print(count_occurrences(arr, len(arr), 2))