'''
Created on 2013/06/27

@author: tsukasahashimoto
'''


import sys
from opcode import *


def name(variable):
    """get argument variable's name."""

    frame = sys._getframe(1)
    co = frame.f_code
    code = co.co_code

    i = 0; n = frame.f_lasti - 2
    oparg = extended_arg = 0

    while i < n:
        c = code[i]
        op = ord(c)

        i = i + 1
        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i + 1]) * 256 + extended_arg
            extended_arg = 0
            i = i + 2
            if op == EXTENDED_ARG:
                extended_arg = oparg * 65536L

    if op in hasconst:
        return co.co_consts[oparg]
    elif op in hasname:
        return co.co_names[oparg]
    elif op in haslocal:
        return co.co_varnames[oparg]
    elif op in hasfree:
        return (co.co_cellvars + co.co_freevars)[oparg]

    raise ValueError('The argument may be syntax. Or unknown error occured.')