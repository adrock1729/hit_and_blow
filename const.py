import itertools as itls

# 取りうるHit and Blowのリスト
HBs = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
       [1, 0], [1, 1], [1, 2], [1, 3],
       [2, 0], [2, 1], [2, 2],
       [3, 0], [4, 0]]

# Hit and Blow game で使用できる全ての数のリスト
AN = list(itls.permutations(range(10), 4))
