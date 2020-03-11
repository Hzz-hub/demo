import random


class Dice:
    def rollnumber(self):
        num = random.randint(1, 6)
        num2= random.randint(1, 6)
        return num, num2


