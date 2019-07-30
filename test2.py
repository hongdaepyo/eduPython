import os

a = [ "test" + str(x) for x in range(5)]

for name in a:
    os.mkdir("../../jittest/" + name);

for name in a:
    os.removedirs(name)
b = os.scandir("c:\\jittest")


for dirs in b:
    c = dirs

import gc

gc.isenabled()


pool = [1, 2, 3]
print(list(map(''.join, itertools.permutations(pool))))