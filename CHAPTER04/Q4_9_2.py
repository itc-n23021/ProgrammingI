import os
import sys

MAX = 2
print(sys.getbefaultencoding())
print(os.path.basename(os.getcwd()))
for i in range(3):
    print(i, end=" ")
    if MAX > i:
        print(MAX)
    else:
        print("#")
