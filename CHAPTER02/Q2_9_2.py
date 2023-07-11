x = True
y = False
z = None

print(x and z is None)
print(not x or not y)
print(x and not y and z is None)

# 上から1、2、3とする
# 1 ＝ True
# 2 ＝ True
# 3 ＝ True
# と出力される
# 1 x = True、'z is None'はz = Noneでis演算子は正しいので'True'となる
# 2 'not x'はx = Trueなので'False'、'not y'はy = Falseなので'True'、(False or Treu)
# 3 1、2より'not = y'は'True'、'z is None'は'True'となる
