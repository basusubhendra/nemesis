#!/usr/bin/python3

import sys
import gmpy2
from pi import pi
from e import e
from threading import Thread
from queue import Queue
def _match_(line, pp, param, q):
    if pp[0] in line and pp[2] in line:
        q.put([param, 1])
    else:
        q.put([param, 0])
    return

def factorize(rnum):
    l = len(rnum)
    bnum = str(bin(int(rnum))[2:])
    f=open("./stripped_zeros.dat","r")
    lines = f.readlines()
    line_number = -1
    count = 0
    ptr = 0
    prod = gmpy2.mpz("1")
    nmatches1 = 0
    nmatches2 = 0
    while True:
        nk = int(rnum[count % l])
        line_number = line_number + nk
        _line_ = lines[line_number].lstrip().rstrip()
        _tuple_ = _line_[ptr:ptr+2]
        if _tuple_ == "00":
            q = Queue()
            t1 = Thread(target=_match_, args=(_line_, pi[line_number-1:line_number + 2], 0, q,  ))
            t2 = Thread(target=_match_, args=(_line_, e[line_number-1:line_number + 2], 1, q,  ))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            c = []
            while not q.empty():
                c.append(q.get())
            input([pi[line_number-1:line_number+2],_line_,e[line_number-1:line_number+2]])
        ptr = (ptr + 1) % 8
        count = count + 1
    f.close()
    return

if __name__ == "__main__":
    num = str(sys.argv[1])
    factors = factorize(num)
