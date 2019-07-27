from optimize_shrink_neighbors import reduction_neighbors, second_ask
from const import HBs
from neighbors import Nhb, intersect
from tqdm import tqdm

first_ask = (0, 1, 2, 3)
third_asks = []
second_red_list = []

for i in range(13):
    [h, b] = HBs[i]
    neighbors = Nhb(first_ask, h, b)
    third_ask_i = []
    print('first ask HB:', h, b)
    for j in tqdm(range(13)):
        [hh, bb] = HBs[j]
        second_neighbors = intersect(neighbors, Nhb(second_ask[j], hh, bb))
        if len(second_neighbors) >= 80:
            ask = reduction_neighbors(second_neighbors, size=5040)
            second_red_list.append([h, b, hh, bb])
        else:
            ask = None
        ask = str([h, b]) + str([hh, bb]) + ' ' + str(ask) + '\n'
        third_ask_i.append(ask)
    third_asks.append(third_ask_i)

with open('third_asks.txt', 'w+') as f:
    print('データを保存中...')
    for i in tqdm(range(13)):
        for result in third_asks[i]:
            f.write(result)

with open('snd_red_list.txt', 'w+') as f:
    second_red_list = list(map(str, second_red_list))
    second_red_list = list(dict.fromkeys(second_red_list))
    f.write(', \n'.join(second_red_list))
