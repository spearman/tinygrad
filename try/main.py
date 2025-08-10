#!/usr/bin/env python3

from pprint import pprint
import tinygrad as tg

def print_tensor(t):
  print('***********')
  #print("DATA:", t.data()[0])
  print("LAZYDATA:\n", t.lazydata)
  print("LAZYDATA:")
  pprint(t.lazydata.__dict__)
  print("TYPE LAZYDATA:", type(t.lazydata))
  if t.lazydata.base:
    print("BASE:")
    pprint(t.lazydata._base.__dict__)
    print("TYPE BASE:", type(t.lazydata._base))
  print("SHAPE:", t.shape)
  print("DTYPE:", t.dtype)
  print("DEVICE:", t.device)
  print("NDIM:", t.ndim)
  print(f"NUMPY:\n{t.numpy()}")

a = tg.Tensor(
  [[1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8],
   [1, 2, 3, 4, 5, 6, 7, 8]])
"""
a = tg.Tensor(
  [[1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7],
   [1, 3, 5, 7]])
"""
print_tensor(a)
a = a.shrink((((2,6), (2,6))))
print_tensor(a)
a = a.pad((((2,2), (1,1))))
print_tensor(a)
#a = a.avg_pool2d(stride=(1))
#print_tensor(a)
#a = a.interpolate((8, ))
#print_tensor(a)
