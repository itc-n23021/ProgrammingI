for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 0から9までの整数から奇数が出力される。

for i in range(10):
    if i % 2 == 0:
        break
    print(i)

# 'continue'を'break'に変更すると、何も表示されない。
