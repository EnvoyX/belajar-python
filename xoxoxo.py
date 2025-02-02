def check(s):
    totalX = 0
    totalO = 0
    result = False
    arr = list(s.lower())
    print(arr)
    for i in range(len(arr)):
        if arr[i] == "x":
            totalX +=1
        elif arr[i] == "o":
            totalO += 1
    if totalX == totalO :
        result = True
    else:
        result = False
    print(result)
    
    
check("ooxx")
check("xooxx")
check("ooxXm")
check("zpzpzpp")
check("zzoo")