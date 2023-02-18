import random

lottery = set({})

while len(lottery) < 6:
    lottery.add(random.randint(1, 50))

lotteryTuple = tuple(lottery)

print(lottery)
print(sorted(lotteryTuple))
