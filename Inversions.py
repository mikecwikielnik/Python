# Returns counts of inversions


def maxInversions(arr):
    n = len(arr)
    icount = 0 
    for i in range(0,n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                for k in range(j+1, n):
                    if arr[j] > arr[k]:
                        icount += 1
    return icount

arr = [4,2,2,1]
maxInversions(arr)

 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

def getInvCount(arr):
    n = len(arr)
    invcount = 0  #Initialize result   
    for i in range(0,n-1):
        for j in range(i+1 , n):
                if arr[i] > arr[j]:
                    for k in range(j+1 , n):
                        if arr[j] > arr[k]:
                            invcount += 1
    return invcount
 
# Driver program to test above function
arr = [4,2,2,1]
getInvCount(arr)
