# Krishna Pandian


#def findMissingSlow(arr):
  #  for x,y in enumerate(arr):
 #       if x != y:
   #         return x
    #    raise ValueError(msg = "No Missing Element")



def findMissing(arr):
    #print(arr)
    lower = 0               #BST Algorithm
    upper = len(arr) - 1
    middle = (lower + upper) // 2   
    while (lower < upper):  #Checks until they lower and upper are equal
        middle = (lower + upper) // 2
        #print("Upper:" + str(upper) + " Lower:" + str(lower) + " Middle:" + str(middle))
        if middle == arr[middle]:   
            lower = middle + 1  #increments lower bound to avoid infinite
        else:
             upper = middle

    middle = (lower+upper) // 2
    if arr[middle] != middle:   #checks if a missing element exists
        return middle
    return -1


if __name__ == "__main__":
    #print([1,2,3,4,5])
    arr = list(range(10000000))
    #print(arr)
    arr.remove(3)
    #print(arr)
    print(findMissing(arr))

