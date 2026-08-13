def binary(arr,low,high,target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    if target < arr[mid]:
        return binary(arr,low,mid-1,target)

    return binary(arr,mid+1,high,target)

arr = [1,2,3,4,5,6,7,8,9]
result = binary(arr,0,len(arr)-1,3)
print(result)