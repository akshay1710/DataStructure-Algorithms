#sorted list using recurssio

def isSorted(a):
    l = len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    smallList = a[1:]
    isSmallerListSorted = isSorted(smallList)
    if isSmallerListSorted:
        return True
    else:
        return False

a = [1,2,4,5,78,99,101,243,3]
print(isSorted(a))
