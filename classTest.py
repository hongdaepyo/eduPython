class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value >= 1000:
            print("value는 1000보다 커질 수 없습니다.")
        else:
            self.value += val

a = MaxLimitCalculator()
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)
a.add(100)

print(a.value)
