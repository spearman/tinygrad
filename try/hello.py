#!/usr/bin/env python3

import os

os.environ["DEBUG"] = "2"
#os.environ["NULL"] = "1"

from tinygrad import Tensor

os.environ["NV"] = "1"
#os.environ["CPU"] = "1"
#os.environ["CLANG"] = "1"
#os.environ["LLVM"] = "1"
#os.environ["GPU"] = "1"

x = Tensor.randn(4, 3, 2)
y = Tensor.randn(2)
z = x.matmul(y)
print(f"z.device: {z.device}")
print(z.numpy())
#print(f"x ({x.shape}):\n{x.numpy()}")
#print(f"y ({y.shape}):\n{y.numpy()}")
#print(f"z = x * y ({z.shape}):\n{z.numpy()}")
