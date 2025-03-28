import sys
import stdio
# Write a program that takes two numbers as command line arguments and prints their sum.
def print_sum():
    num_one = sys.argv[1]
    num_two = sys.argv[2]

    stdio.write(f"{float(num_one) + float(num_two)}\n")