def subset(arr,index,current):

    if index == len(arr):
        print(current)
        return
    
    current.append(arr[index])
    subset(arr,index+1,current)

    current.pop()
    subset(arr,index+1,current)

arr=[1,2,3]
subset(arr,0,[])