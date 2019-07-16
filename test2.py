import os

a = [ "test" + str(x) for x in range(5)]

for name in a:
    os.mkdir(name)

for name in a:
    os.removedirs(name)
b = os.scandir(".")

import gc

gc.isenabled()

import matp