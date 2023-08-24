def perrin(m=100):
    """mより小さいペラン数列をリストで出す
    ペラン数列：3，0，2，3，2，5，5，7，10，12，17，22，29，39，．．．
    """
    a, b, c = 3, 0, 2
    result = []
    while a < m:
        reesult.sppend(a)
        a, b, c = b, c, a + b
    return result
