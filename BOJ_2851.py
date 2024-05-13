pre_nsum = 0
nsum = 0
num = 0

for _ in range(10):
    num = int(input())
    pre_nsum = nsum
    nsum += num
    if nsum >= 100:
        if (nsum - 100) <= (100 - pre_nsum):
            print(nsum)
            break
        elif (nsum - 100) > (100 - pre_nsum):
            print(pre_nsum)
            break

    
# pre_nsum = 0
# nsum = 0
# num = 0

# for _ in range(10):
#     num = int(input())
#     pre_nsum = nsum
#     nsum += num
#     if nsum >= 100:
#         # if (nsum - 100) <= (100 - pre_nsum):
#         #     print(nsum)
#         #     break
#         if (nsum - 100) > (100 - pre_nsum):
#             nsum = pre_nsum
#             break
# print(nsum)