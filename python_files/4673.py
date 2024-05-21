'''
Way 1. 생성자를 만든 다음, 10000까지 중에서 생성자들 제외해서 print
Way 2. 아라토스테네스의 채와 비슷하게 -> O(N)
'''

# Make True for 10,000 counts
truth_table = [True for _ in range(10000)]
org_num = 1
while org_num < 10000:
    num = org_num
    while num < 10000:
        str_num = str(num) # str type 1234
        for i in range(len(str_num)): # 4 times
            temp = int(str_num[i]) # 1, 2, 3, 4
            num += temp
        if num-1 < 10000:
            truth_table[num-1] = False
    org_num += 1

for idx, truth in enumerate(truth_table):
    if truth == True:
        print(idx+1)