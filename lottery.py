import random

EACH_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45



quick_picks = int(input("how many quick picks you want? "))
while quick_picks <=0:
    print("not a valid pick")
    quick_picks = int(input("how many quick picks you want? "))

for i in range(quick_picks):
    picks = []
    for j in range(EACH_LINE):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        while random_number in picks:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        picks.append(random_number)
    picks.sort()
    print(" ".join("{:2}".format(random_number) for random_number in picks))


