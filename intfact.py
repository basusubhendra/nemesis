#!/usr/bin/python3

import sys
from pi import pi
from e import e

def factorize(rnum):
    l = len(rnum)
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    f.close()
    line_number = -1
    count = 0
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        input([pi[line_number-1:line_number+2],_line_,e[line_number-1:line_number+2]])
        count = count + 1
    return

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
