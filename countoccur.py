def countoccur(arr,n,target):
    if n == 0:
        return 0

    count = countoccur(arr,n-1,target)

    if arr[n   1] == target:
        count += 1

        return count
    
arr = [1,2,3,4,5,2,2,6,7]

print(countoccur(arr,len(arr),2))

