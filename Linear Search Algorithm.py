def linearsearch(list,key):
    i=0
    while i< len(list):
        if list[i]==key:
          return True, f"index is {i}"
        else:
            i+=1
    return False, f"No such element is found "

list  = [84,21,47,96,15]
print(linearsearch(list,15))
print(linearsearch(list,90))
print(linearsearch(list,47))
print(linearsearch(list,100))

