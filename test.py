import random

tupli = [(10, 30), (13, 70), (7, 9), (12, 45)]
i = 1

choice = random.randint(0, tupli.__len__() - 1)


print(choice, tupli[choice])