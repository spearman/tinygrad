#!/usr/bin/env python3

import os

os.environ["DEBUG"] = "2"
#os.environ["NULL"] = "1"

from tinygrad import Tensor

#os.environ["DEV"] = "NV"
#os.environ["DEV"] = "CPU"
os.environ["DEV"] = "CUDA"
#os.environ["DEV"] = "CL"

x = Tensor.randn(4, 3, 2)
y = Tensor.randn(2)
z = x.matmul(y)
print(f"z.device: {z.device}")
print(z.numpy())
#print(f"x ({x.shape}):\n{x.numpy()}")
#print(f"y ({y.shape}):\n{y.numpy()}")
#print(f"z = x * y ({z.shape}):\n{z.numpy()}")
