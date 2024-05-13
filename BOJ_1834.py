def solutions(num):
    max_num = num * (num-1) + (num-1)
    a = num+1
    result = 0
    while a <= max_num:
        a1 = a // num
        a2 = a % num
        if a1 == a2: 
            # print(a, end=' ')
            result += a
        a += (num+1)
    return result

N = int(input())
print(solutions(N))
