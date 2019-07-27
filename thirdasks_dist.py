from optimize_shrink_neighbors import second_ask
from const import HBs
from neighbors import Nhb, intersect


if __name__ == "__main__":
    # 0123を最初の質問として、
    # reduction_neighborsによる2回目の最適な質問に対し、
    # さらに3回目の質問の一部をreduction_neighborsによって探す
    # そのためにまずは分布を見る
    ask_first = (0, 1, 2, 3)
    for i in range(14):
        dist = []
        [h, b] = HBs[i]
        hb = str(h) + ',' + str(b)
        neighbor = Nhb(ask_first, h, b)
        for [h, b] in HBs:
            d = len(intersect(neighbor, Nhb(second_ask[i], h, b)))
            dist.append(d)
        print(hb, ':')
        print('hit 0:', dist[:5])
        print('hit 1:', dist[5:9])
        print('hit 2:', dist[9:12])
        print('hit 3:', dist[12])
        print('hit 4:', dist[13])
        print('')
