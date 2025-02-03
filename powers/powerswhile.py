import sys
import stdio

arg_v = int(sys.argv[1])
index = 0
while arg_v >= index:
    stdio.write(f"{index} {index**2}\n")
    index += 1
    