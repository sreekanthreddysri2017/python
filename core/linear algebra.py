import numpy as np
from numpy import linalg as li

N = int(input())
arr = np.array([input().split() for _ in range(N)],dtype = 'f')
print(round(li.det(arr),2))