''' 10 6 
2 1 9 2 3 7 (2) 1 2 4

1. Brute force
Max #100
Max counting = 100 + 99 + 98 ... + 1 = 5050 < 1 Billion

    1) Front num vs Rest of all
    2-1) If F.N is biggest, print
        2-1-1) If it is target num && idx == 0, result +1, break and print the result
        2-1-2) If not, do it again and result +1
    2-2) If F.N is smaller, rotate

Problem
    How can remember the target?
    - Remember the index num 
    - If the queue elements removed, adjust the number
        1) Smaller than index num >> Tear down size and index
        2) Bigger than index num >> Tear down size
'''
# 2 1 9 2 3 7 2 1 2 4
# 2 1 9 2 3 7 (2) 1 2 4 >> 0
# 2 1 2 3 7 (2) 1 2 4 >> 1
# 2 1 2 3 (2) 1 2 4 >> 2
# 2 1 2 3 (2) 1 2 >> 3
# 2 1 2 (2) 1 2 >> 4
# 2 1 2 1 2 >> 5. Finished!

def print_priority():
    total = list(map(int, input().split())) 
    size = total[0]
    idx = total[1]
    pointer = 0 # for pointing num_list
    result = 0 # for printing order result
    num_list = list(map(int, input().split())) # Set the print idx

    while True:
        if pointer > size-1: 
            pointer = 0
        if (num_list[pointer] == max(num_list)) and (idx == pointer):
            result += 1
            break
        elif num_list[pointer] == max(num_list):
            # print(f"Max num {num_list[pointer]} printed at pointer {pointer}")
            size -= 1
            result += 1
            if pointer < idx:
                idx -= 1
            elif pointer > idx:
                pass
            del num_list[pointer]
        elif num_list[pointer] < max(num_list):
            # print("Lower than max")
            pointer += 1

    # print(f"Finally {num_list[pointer]} printed as an order of {result}!")
    return result

get_rot = int(input())
for _ in range(get_rot):
    print(print_priority())


