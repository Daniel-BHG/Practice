num = int(input("Press num : "))
num_list = []
for _ in range(num):
    num_list.append(int(input("Check : ")))
num_list = sorted(num_list)
for i in num_list:
    print(i)