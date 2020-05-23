import os
import glob



for file in glob.glob("sd//pmd/*.pmd"):
    pmd = open(file, "rb")
    x = 0
    print ("{0: <20} ".format(file), end = " ")
    while x < 28:
        b = pmd.read(1)
        print ("{0:0=3d} ".format(ord(b)), end =" ")
        x = x + 1

    print ("")


