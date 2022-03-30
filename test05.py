class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, a):
        self.value += a

class UpgradeCalculator(Calculator):
    def minus(self, a):
        self.value -= a

cal = UpgradeCalculator()
print(cal.add(19))
print(cal.minus(7))