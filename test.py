
def getCdList(*args):
        glist = set()
        for arg in args:
                for i in range(1, arg + 1):
                        if arg % i == 0:
                                glist.add(i)
        return glist

def getGcd(cdList):
        return max(cdList)

def getlcm(gcd, *args):
        lcm = 0;
        for arg in args:
                lcm = arg / gcd
        


cdList = getCdList(10 ,15 ,20)
print("cdList = ", cdList)
gcd = getGcd(cdList)
print("gcd = ", gcd)
lcm = getlcm(gcd, 10, 15, 20)