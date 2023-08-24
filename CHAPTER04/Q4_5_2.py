s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def str_to_float_coordi(s_coordi):
    """与えられた文字列をコンマで分割してfloat型に変換して数値を返す"""
    p = s_coordi.split(",")
    return list(map(float, p))


def str_to_float_coordi_iter(s_coordi_list):
    """与えられたリストの要素をstr_to_float_coordi() 関数で処理して結果の反復可能体を返す"""
    return map(str_to_float_coordi, s_coordi_list)


f_coordi_list = list(str_to_float_coordi_iter(s_coordi_list))

print(f_coordi_list)
