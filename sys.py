import sys
import os

sys.modules.keys()

sys.path # list of paths where to look for a module.


if __name__ == "__main__":
     r = sys.modules.keys() # returns names of all imported libraries
     print(r)