def sumArray(arr):
    # Please add your code here
    l = len(arr)
    if l==0:
        return sum
    else:
        return arr[0] + sumArray(arr[1:])

# Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
# #print(sumArray(arr))

#Find Value in Some
def FindValue(arr, x):
    l = len(arr)
    if l==1:
        return False
    if arr[0] == x:
        print(arr[0])
        return True
    else:
        return FindValue(arr[1:], x)

arr = [3,4,2,6,7,8]
x = 7
print(FindValue(arr,x))