
def print_1_to_10(n):
    if n==0:
        return 1
    else:
        print_1_to_10(n-1)
        print(n)
        return

#x = print_1_to_10(10)


"...................................................Add Number in Recursion......................................................................................"

def addNum(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    else:
        x = addNum(arr[1:])

        return arr[0] + x

print(addNum([2,3,4,5,6,7]))