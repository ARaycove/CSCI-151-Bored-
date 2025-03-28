import stdio
import sys

n = int(sys.argv[1])
n = n ** 1000
print(n)
i = 0
while i < n:
    stdio.write(f"{i}/{n}\n\n")
    i += 1