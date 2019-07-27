from const import HBs, AN
from calculateHB import HB
from random import sample
from math import log2


# 分布に対するエントロピーの定義
def entropy(dist, eps=1e-8):
    return -1 * sum([d*log2(d + eps) for d in dist])


# neighbor(HBの値から計算される答えの可能性がある選択肢全体、近傍)
# に対するエントロピーの定義
def neighbors_entropy(num, neighbor):
    size = len(neighbor)
    hb_lens = []
    for hb in HBs:
        hb_li = [x for x in neighbor if HB(num, x) == hb]
        hb_lens.append(len(hb_li))
    dist = [float(hb_len)/size for hb_len in hb_lens]
    return entropy(dist)


# 近傍に対するエントロピーを計算し、エントロピーの最も大きい質問を返す
def reduction_neighbors(neighbors, verbose=False, size=1000):
    count = 1
    if size > 5040:
        size = 5040
    poss_nums = sample(AN, size)
    max_arg = poss_nums[0]
    max_entropy = neighbors_entropy(max_arg, neighbors)
    errors = []
    for x in poss_nums[1:]:
        count += 1
        try:
            ent = neighbors_entropy(x, neighbors)
            if ent > max_entropy:
                max_arg = x
                max_entropy = ent
        except ValueError:
            errors.append(x)
        except IndexError:
            errors.append(x)

        if verbose:
            if (count % (size//10)) == 0:
                print("%d" % ((100*count)//size), '%')
    print(max_arg, max_entropy)
    return max_arg


# 計算量縮小のためあらかじめsecond_asks.txtに
# reduction_neighborsで計算した２つ目の質問を保存
second_ask = [
    (7, 9, 5, 6),
    (5, 8, 6, 1),
    (2, 9, 4, 1),
    (7, 2, 9, 0),
    (2, 8, 0, 1),
    (6, 1, 9, 8),
    (4, 1, 2, 6),
    (8, 0, 4, 3),
    (6, 3, 2, 1),
    (1, 4, 2, 7),
    (1, 5, 4, 3),
    (5, 1, 0, 6),
    (0, 2, 7, 5),
    (0, 5, 9, 4)
]
