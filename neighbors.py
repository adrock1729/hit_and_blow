from calculateHB import HB
from const import AN


# リストの共通部分をとる。
def intersect(l1, l2):
    return list(filter(lambda x: x in l1, l2))


# 複数のリストの共通部分をとる関数
def inter_neighbors(neighbors):
    l1 = neighbors[0]
    for l2 in neighbors[1:]:
        l1 = intersect(l1, l2)
    return l1


# xとのHB値がh, bになる様な値のリストを返す
def Nhb(x, h, b):
    return [y for y in AN if HB(y, x) == [h, b]]
