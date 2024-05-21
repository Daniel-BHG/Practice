# Edge case : aaaaaaaaaaaabbc -> 12a2bc -> 6

'''
# slist = []
# for i in range(lth//2+1):
#     if i*2 >= lth:
#         pass
#     else: slist.append(s[i*2 : (i+1)*2])
# print(slist)

# slist = []
# for i in range(lth//3+1):
#     if i*3 >= lth:
#         pass
#     else:
#         slist.append(s[i*3 : (i+1)*3])
# print(slist)

# slist = [] # Until lth//2
# for i in range(lth//7+1):
#     if i*7 >= lth:
#         pass
#     else:
#         slist.append(s[i*7 : (i+1)*7])
# print(slist)
'''

s = input()
# s = "xababcdcdababcdcd"
# 반례 = aaaaaaaaaaa ... 10개 이상일 때

# Step 2. Check if same and print min
def is_same(lst, k):
    cnt = 1
    des = 0 # Minus할 정도
    len_lst = len(lst)
    for i in range(len_lst-1):
        if lst[i] == lst[i+1]:
            cnt += 1
        else: 
            if 2 <= cnt < 10:
                des += -k*(cnt-1)+1
                cnt = 1
            elif 10 <= cnt < 100:
                des += -k*(cnt-1)
                cnt = 1
            elif 100 <= cnt < 1000:
                des += -k*(cnt-1)-1
                cnt = 1
            elif 1000 == cnt:
                des += -k*(cnt-1)-2
                cnt = 1
    if lst[len_lst-2] == lst[len_lst-1]: 
        if cnt >= 2:
            des += -k*(cnt-1)+1
            cnt = 1
        elif 10 <= cnt < 100:
                des += -k*(cnt-1)
                cnt = 1
        elif 100 <= cnt < 1000:
            des += -k*(cnt-1)-1
            cnt = 1
        elif 1000 == cnt:
            des += -k*(cnt-1)-2
            cnt = 1
    return des


def solution(s):
    lth = len(s)
    slist = []
    check_min = []

    # Step 1. Slicing
    for i in range(1, lth//2+1):
        slist = []
        if i == 1: 
            slist = list(s)
            # print(slist)
            des = is_same(slist, i)
            check_min.append(lth + des)
        else:
            for j in range(lth//i+1):
                if j*i >= lth:
                    pass
                else:
                    slist.append(s[j*i : (j+1)*i])
            # print(slist)
            des = is_same(slist, i)
            check_min.append(lth + des)

    print(check_min, min(check_min))
    return min(check_min)

print(solution(s))
