def palin(n,left,right):

    if left >= right:
        return True

    if n[left] != n[right]:
        return False

    return palin(n,left+1,right-1)

s="madam"

print(palin(s,0,len(s)-1))