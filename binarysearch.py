def binarysearch(number):
    list1 = range(20, 100)
    i = 0
    j = len(list1)-1
    while i < j:
        mid = (i + j) // 2
        if number > list1[mid]:
            i = mid + 1
        else:
            j = mid - 1
    print('Number at index:', mid)
    return mid
    
call = binarysearch(56)

