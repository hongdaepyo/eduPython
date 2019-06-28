# python myargv.py 1 2 3 4 5 6 7 8 9 10 으로 실행

import sys

print(sum(list(map(lambda x: int(x), sys.argv[1:]))))