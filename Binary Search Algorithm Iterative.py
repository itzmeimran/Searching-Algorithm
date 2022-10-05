def BSA(a,k):
    low = 0
    high = len(a)-1
    while low<=high:
        mid = (high+low)//2
        if k == a[mid]:
            return True
        elif k < a[mid]:
            high = mid-1
        else:
            low = mid+1
    return False
a = [1,3,5,7,100]
print(BSA(a,7))
print(BSA(a,99))