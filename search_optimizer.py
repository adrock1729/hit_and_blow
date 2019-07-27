from optimize_shrink_neighbors import reduction_neighbors
from const import HBs
from neighbors import Nhb

# 0123を最初の質問として、
# reduction_neighborsによる2回目の最適な質問を計算し
# その計算結果をsecond_asks.txtに保存する
if __name__ == "__main__":
    ask_first = (0, 1, 2, 3)
    neighbors = {}
    optimized_second_asks = {}
    for i in range(14):
        [h, b] = HBs[i]
        neighbors[i] = Nhb(ask_first, h, b)
        second_ask = reduction_neighbors(
            neighbors=neighbors[i],
            verbose=True,
            size=5040
            )
        optimized_second_asks[i] = second_ask
    with open('second_asks.txt', 'w+') as f:
        for i in range(14):
            [h, b] = HBs[i]
            result = "{}, {}, {}\n".format(h, b, optimized_second_asks[i])
            f.write(result)
