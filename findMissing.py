# Krishna Pandian


#def findMissingSlow(arr):
  #  for x,y in enumerate(arr):
 #       if x != y:
   #         return x
    #    raise ValueError(msg = "No Missing Element")



def findMissing(arr):
    lower = 0               #BST Algorithm
    upper = len(arr) - 1
    middle = (lower + upper) // 2   
    while (lower < upper):  #Checks until they lower and upper are equal
        #print("Upper:" + str(upper) + " Lower:" + str(lower) + " Middle:" + str(middle))
        middle = (lower + upper) // 2
        if middle == arr[middle]:   
            lower = middle + 1  #increments lower bound to avoid infinite
        else:
             upper = middle
             
    if arr[middle] != middle:   #checks if a missing element exists
        return middle
    raise ValueError(msg ="No missing element")
    return -1


#if __name__ == "__main__":
    #print([1,2,3,4,5])
    #print(findMissing([0,1,2,3,5,6,7]))

