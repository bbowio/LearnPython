import numpy as np
def seq(l=0,h=1,c=10,m=10):
    seq1 = np.linspace(l,h,c)
    print("Sequence 1: ", seq1)
    c2 = c * m
    seq2 = np.linspace(l, h, c2)
    print("Sequence 2: ", seq2)