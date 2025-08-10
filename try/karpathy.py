#!/usr/bin/env python3

from tinygrad import Tensor

a = Tensor(2.0)
b = Tensor(-3.0)
c = Tensor(10.0)
e = a * b
d = e + c
f = Tensor(-2)
L = d * f
print(L.numpy())
