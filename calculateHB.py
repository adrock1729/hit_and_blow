# HIT値の計算関数定義
def Hit(a, b):
    return len([i for i in range(4) if a[i] == b[i]])


# BLOW値の計算関数定義
def Blow(a, b):
    return len([i for i in range(4) if a[i] in b]) - Hit(a, b)


# Hit and Blow(HB)の値をリスト出力
def HB(a, b):
    return [Hit(a, b), Blow(a, b)]


# 値aとnum_listの値のHBをリスト出力
def HBlist(a, num_list):
    return [HB(a, x) for x in num_list]
