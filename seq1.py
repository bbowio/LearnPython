import numpy as np
def seq(l=0,h=1,c=10,m=10):
    np.set_printoptions(threshold=999999)
    i = 1
    while i < 10:
        seq = np.linspace(i, i+2, i*10)
        print("Sequence ", i, " :", seq, end="\r")
        i += 1