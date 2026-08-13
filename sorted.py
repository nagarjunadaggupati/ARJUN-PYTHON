def sorted(arr , n ):
    if n <= 1:
        return True

    if arr[n-1] < arr[n-2]:
        return False
    return sorted(arr, n-1)

arr = [1,2,3,4,5,6]
print(sorted(arr,len(arr)))