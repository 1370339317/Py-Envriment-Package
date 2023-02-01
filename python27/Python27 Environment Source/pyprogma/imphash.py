# encoding: utf-8
import os
import sys
import pefile

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("../")
    print(pefile.PE(sys.argv[1]).get_imphash())
