def fib2(n):
    """nより小さいフィボナッチ数列を返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


fib2(1000)
