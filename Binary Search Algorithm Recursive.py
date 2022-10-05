Works only on sorted list
def BSA(list,key,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if key == list[mid]:
            return True
        elif key < list[mid]:
            return BSA(list,key,low, mid-1)
        else:
            return BSA(list,key,mid+1,high)
               
              

list = [1,3,5,7,100]
print(BSA(list,7,0,5))  
print(BSA(list,25,0,5))



