#!/usr/bin/env python3

from tinygrad.renderer.cstyle import MetalRenderer
from tinygrad.renderer.cstyle import OpenCLRenderer
from tinygrad.renderer.cstyle import CUDARenderer
from tinygrad.ops import UOp, Ops
from tinygrad import dtypes

const = UOp(Ops.CONST, dtypes.float, arg=1.0)
add = UOp(Ops.ADD, dtypes.float, src=(const, const), arg=None)

print(add)
#print(MetalRenderer().render([const, add]))
print(OpenCLRenderer().render([const, add]))
#print(CUDARenderer("sm_90").render([const, add]))
#print(MetalRenderer().render([
#  UOp(Ops.SPECIAL, dtypes.int, arg=("gidx0", 16))
#]))
print(OpenCLRenderer().render([
  UOp(Ops.SPECIAL, dtypes.int, arg=("gidx0", 16)),
  UOp(Ops.SPECIAL, dtypes.int, arg=("gidx1", 16))
]))
