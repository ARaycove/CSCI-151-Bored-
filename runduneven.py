import sys
import stdio

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

while not stdio.isEmpty():
    value = stdio.readInt()
    if is_even(value):
        stdio.writeln(value)