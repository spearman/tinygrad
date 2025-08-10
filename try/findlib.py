#!/usr/bin/env python3

import ctypes.util

clib = ctypes.util.find_library('clang')

print(clib)
