#python Recursion


def fact(n):
    if n == 0:
        print("running")
        return 1

    return n * fact(n-1)

x = fact(5)
print(x)

# recursion Find First Index
def firstIndex(arr, x):
    # Please add your code here]
    l = len(arr)
    if l == 0:
        return -1
    if arr[0] == x:
        print("arry")
        return 0

    smallIndex = firstIndex(arr[1:],x)
    print(smallIndex)
    if smallIndex == -1:
        return -1
    else:
        return smallIndex + 1
print(
    firstIndex([2,3,5,6,7,4,7,55,5], 5)
)

# Find the index using recurssion in specific location si
def firstIndexB(arr,x,si):
    if len(arr)==si:
        return -1
    if arr[si] == x:
        print(si)
        return si
    smallIndex = firstIndexB(arr,x,si+1)
    print('SMALL')
    return smallIndex
print(
    firstIndexB([2, 3, 5, 6, 7, 4, 7, 55, 5], 5,0)
)

#find the index using recursion in last to start
## Print output as specified in the question.
def LastIndex(arr,x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[-1]==x:
        return l - 1
    smallIndex = LastIndex(arr[:l-1],x)
    if smallIndex == 0:
        return -1
    return smallIndex
print(LastIndex([2,3,4,5,6,2,3], 2))


def lastIndex(a, x):
    l = len(a)
    if l == 0:
        return -1
    smallerList = a[1:]
    smallerListOutput = lastIndex(smallerList, x)
    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


def lastIndexB(a, x, si):
    l = len(a)
    if si == l:
        return -1
    smallerListOutput = lastIndexB(a, x, si + 1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return si
        else:
            return -1


a = [1, 4, 5, 4, 8]
x = 4
print(lastIndex(a, x))
print(lastIndexB(a, x, 0))