def digital_root(n):
    n = str(n)
    n = list(map(int,n))
    print(n)
    result = 0
    for num in n:
        result += num   
    if (result > 9):
        return digital_root(result)  
    return result

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))