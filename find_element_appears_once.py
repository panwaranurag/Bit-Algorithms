def getSingle(arr, n):
    result = 0
    for i in range(0,32):
        sum = 0
        x = (1 << i)
        for j in range(0,n):
            if (arr[j] & x):
                sum += 1
        if sum % 3:
            result |= x
    return result

if __name__ == "__main__":
    arr = [12,1,12,3,12,1,1,2,3,2,2,3,7]
    n = len(arr)
    print "Length of array", n
    print "The element with single occurance is", getSingle(arr,n)