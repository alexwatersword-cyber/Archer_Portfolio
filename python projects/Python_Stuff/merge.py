import random
#creat a list of random numbers
def createListOfRandomNumbers():
    rNum = []
    for _ in range(10):
        rNum.append(random.randint(-1000,1000))
    return rNum

def split(lst):
    if (len(lst) > 1):
        middle = len(lst)//2
        left = lst[:middle]
        right = lst[middle:]
        split(left)
        split(right)
        merge(lst, left, right)

def merge(original, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            original[k] = left[i]
            i += 1
        else:
            original[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        original[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        original[k] = right[j]
        j += 1
        k += 1

def mergeSort(a):
    split(a)

def main():
    rlist = createListOfRandomNumbers()
    print(rlist)
    mergeSort(rlist)
    print(rlist)

main()