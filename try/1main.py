#!/usr/bin/env python3

from pprint import pprint
import tinygrad as tg

def print_tensor(t):
  print('***********')
  #print("DATA:", t.data()[0])
  print("LAZYDATA:")
  pprint(t.lazydata.__dict__)
  print("TYPE LAZYDATA:", type(t.lazydata))
  if t.lazydata._base:
    print("BASE:")
    pprint(t.lazydata._base.__dict__)
    print("TYPE BASE:", type(t.lazydata._base))
  print("SHAPE:", t.shape)
  print("DTYPE:", t.dtype)
  print("DEVICE:", t.device)
  print("NDIM:", t.ndim)
  print("NUMPY:", t.numpy())


#a = tg.Tensor.randn(20)[2:2+9].reshape(3, 3).pad((None, (0, 2)))#.shrink((None, (0, 4)))
a = tg.Tensor.ones(8)
print_tensor(a)
print("CONTIGUOUS:", a.lazydata.st.views[0].contiguous)
a = a.contiguous()
print_tensor(a)
print("CONTIGUOUS:", a.lazydata.st.views[0].contiguous)

b = tg.Tensor.randn(24)
print_tensor(b)

c = tg.Tensor(None)
print_tensor(c)
