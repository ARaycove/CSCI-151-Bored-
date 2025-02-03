import stdio
import sys
import random

num_flips = int(sys.argv[1])
heads = 0
tails = 0

for _ in range(num_flips):
    result = random.randint(0, 1)
    if result == 0:
        heads += 1
    else:
        tails += 1

stdio.write(f"Out of {num_flips} coin flips\n")
stdio.write(f"Heads = {heads}\n")
stdio.write(f"Tails = {tails}\n")
stdio.write(f"{heads/num_flips} vs {tails/num_flips}\n")
