a = {x for in 'abcabcabc' if x not in 'ab'}
b = {y for in 'abcabcabc' if y not in 'bc'}
a | b

# {'q','c'}  が出力される
