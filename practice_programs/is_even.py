import stdio
import sys

input_val = int(sys.argv[1])
second_input_value = int(sys.argv[2])

for i in range(input_val, second_input_value+1):
    if ((i / 2) - (i // 2)) == 0:
        stdio.write(f"Is {i} Even?\n")
        