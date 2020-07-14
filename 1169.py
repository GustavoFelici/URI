import numpy as np

n = int(input())
for i in range (0,n):
    x = int(input())
    print(str(np.uint64(pow(2, x) / 12000)), "kg")