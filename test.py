from const import AN
from calculateHB import HB
from neighbors import Nhb, intersect
from random import shuffle
from tqdm import tqdm
from optimize_shrink_neighbors import second_ask
from snd_red_list import snd_red_hblist, snd_red_numlist

if __name__ == '__main__':
    # 平均スコアの計算をする
    # targetの数
    num = 500
    # 総質問回数
    score = []
    # reduction_neighborsを使うHB値の条件
    red_list = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2]]
    # 最大質問回数
    max = 1
    # 正しい答えに行き着いているかのチェック
    # 正しければ　＋１される
    check = 0
    # targetをANから取得する前にANをシャッフルするか
    shuffle_num = True
    an = AN
    if shuffle_num:
        shuffle(an)
    for target in tqdm(an[:num]):
        x = (0, 1, 2, 3)
        count = 1
        [h, b] = HB(target, x)
        hbs = [h, b]
        neighbors = Nhb(x, hbs[0], hbs[1])
        # print('%d 回目の質問:' % count, x)
        # print('Hit and Blow:', h, b)
        # print('Neighbors size:', len(neighbors))
        while h != 4:
            count += 1
            if hbs in red_list and count == 1:
                i = 5 * h + b
                x = second_ask[i]
            elif hbs in snd_red_hblist:
                i = snd_red_hblist.index(hbs)
                x = snd_red_numlist[i]
            else:
                x = neighbors[0]
            [h, b] = HB(target, x)
            hbs = hbs + [h, b]
            neighbors = intersect(neighbors, Nhb(x, h, b))
            # print('%d 回目の質問:' % count, x)
            # print('Hit and Blow:', h, b)
            # print('Neighbors size:', len(neighbors))
        if count > max:
            max = count
        score.append(count)
        check += int(target == x)
    print('平均質問回数: ', sum(score) / num, '回')
    print('最大質問回数: ', max)
    print('error:', num - check)

    for i in range(1, max+1):
        print('質問回数', i, '回: ', score.count(i))
