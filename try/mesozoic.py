#!/usr/bin/env python3

import os

#os.environ["DEBUG"] = "4"

from tinygrad import Tensor

#os.environ["CPU"] = "1"
#os.environ["CLANG"] = "1"
#os.environ["LLVM"] = "1"
os.environ["GPU"] = "1"
#os.environ["NULL"] = "1"

a = Tensor.empty(4, 4)
b = Tensor.empty(4, 4)
z = a + b
print("LAZYDATA:\n", z.lazydata)
print(z.tolist())
print("LAZYDATA:\n", z.lazydata)
