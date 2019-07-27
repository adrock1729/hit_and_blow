from const import HBs, AN
from calculateHB import HB
from neighbors import Nhb, intersect
from random import sample, shuffle
import numpy as np
from tqdm import tqdm


def entropy(dist, eps=1e-8):
    return -1 * sum([d*np.log2(d + eps) for d in dist])


def neighbors_entropy(num, neighbor):
    size = len(neighbor)
    hb_lens = []
    for hb in HBs:
        hb_li = [x for x in neighbor if HB(num, x) == hb]
        hb_lens.append(len(hb_li))
    dist = [float(hb_len)/size for hb_len in hb_lens]
    return entropy(dist)


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
    # print(max_arg, max_entropy)
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


if __name__ == '__main__':
    # 平均スコアの計算をする
    # targetの数
    num = 5040
    score = 0
    red_list = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1]]
    shuffle_num = True
    an = AN
    max = 1
    check = 0
    if shuffle_num:
        shuffle(an)
    # verbose_count = 0
    for target in tqdm(an[:num]):
        x = (0, 1, 2, 3)
        count = 1
        [h, b] = HB(target, x)
        neighbors = Nhb(x, h, b)
        # print('%d 回目の質問:' % count, x)
        # print('Hit and Blow:', h, b)
        # print('Neighbors size:', len(neighbors))
        while h != 4:
            if [h, b] in red_list and count == 1:
                i = 5 * h + b
                x = second_ask[i]
            else:
                x = neighbors[0]
            [h, b] = HB(target, x)
            neighbors = intersect(neighbors, Nhb(x, h, b))
            if h != 4:
                count += 1
            # print('%d 回目の質問:' % count, x)
            # print('Hit and Blow:', h, b)
            # print('Neighbors size:', len(neighbors))
        if count > max:
            max = count
        score += count
        check += int(target == x)
    print('平均質問回数: ', score / num, '回')
    print('最大質問回数: ', max)
    print('error:', num - check)
