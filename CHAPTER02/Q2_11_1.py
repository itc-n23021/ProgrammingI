a, b, c, d = 1, 2, 3, 4
a, b, c, d = c, d, a, b
print(c)

# 答えは「1」になる。
# 2つ目の行で「c = a」となる。1つ目の行で「a = 1」となる。「c = a = 1」よって「c = 1」となる
