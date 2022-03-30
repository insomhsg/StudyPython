# import mod1
# print(mod1.add(3,4))
from mod1 import add
print(add(3,4))

test = list(filter(lambda x: x>0, [1,-3,2,0,-5,6]))
print(test)

class Bird:
    def fly(self):
        raise NotImplementedError