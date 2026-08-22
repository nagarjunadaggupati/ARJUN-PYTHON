def subsequence(s , index , current):
    if len(s) == index:
        print(current)
        return

    subsequence(s , index + 1 , current + s[index])

    subsequence(s , index + 1 , current)

subsequence("abc" , 0 , "")