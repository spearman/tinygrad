#!/usr/bin/env python3

from tinygrad.shape.view import View

v = View.create(shape=(2,2), strides=(2,1))

idx, valid = v.to_indexed_uops()

print("IDX:\n", idx)
print("IDX TYPE:", type(idx))
print("IDX RENDER:\n", idx.render())
print("IDX RENDER TYPE:\n", type(idx.render()))
print("VALID:\n", valid)
