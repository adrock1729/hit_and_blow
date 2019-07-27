from const import AN
from calculateHB import HB
from neighbors import Nhb, intersect
from random import shuffle
from tqdm import tqdm
from optimize_shrink_neighbors import second_ask

if __name__ == '__main__':
    # 平均スコアの計算をする
    # targetの数
    num = 1000
    # 総質問回数
    score = []
    # reduction_neighborsを使うHB値の条件
    red_list = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1]]
    # 最大質問回数
    max = 1
    # 正しい答えに行き着いているかのチェック
    # 正しければ　＋１される
    check = 0
    # targetをANから取得する前にANをシャッフルするか
    shuffle_num = False
    an = AN
    if shuffle_num:
        shuffle(an)
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
            count += 1
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

    for i in range(1, max):
        print('質問回数', i, '回: ', score.count(i))
