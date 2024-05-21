N = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(N)]
time_list.sort(key = lambda x : (x[1], x[0]))
# print(time_list)
# (1, 3) (2, 3) (4, 5) (7, 11)

count = 1
finish_time = time_list[0][1]
for time in time_list[1:]:
    if finish_time <= time[0]:
        count += 1
        finish_time = time[1]

print(count)