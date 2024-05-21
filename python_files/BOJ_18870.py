'''
1. Just find index in for loop -> Time out
    Input and make list = O(N)
    Set creation and sorting = O(N) + O(NlogN) ~= O(NlogN)
    Indexing the loop = for loop O(N) * index method O(N) = Worst O(N^2)
    O(N^2) = O(1e12) ~= 1000s

2. Using dictionary
    Input and make list = O(N)
    Set creation and sorting = O(N) + O(NlogN) ~= O(NlogN)
    Create dict = O(N)
    Find i in dict = O(1)
    Thus, totally, O(NlogN)
'''

N = int(input())
X = list(map(int, input().split()))
X1 = sorted(set(X))
index_map = {value:idx for idx, value in enumerate(X1)}

for i in X:
    print(index_map[i], end=' ')
    # Dict는 list와 다르게, value로 바로 접근 가능