import numpy as np
"""
a=np.array([[2,4,6,8],[1,2,3,4],[3,6,9,12]])
print(a[0:4,0:4])
print(type(a))
print(np.shape(a))
print(np.size(a))
print(np.ndim(a))
print(a.dtype)
"""
a=np.array([2,4,6,8,10,12,14,16,18,20])
print(a.dtype)
print(a.size)
print(a.shape)
print(a.ndim)
print(a.astype(float))
print(len(a))       