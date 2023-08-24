def fib(n):
    """nより小さなフィボナッチ数列を表示する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
        fib(1000)
