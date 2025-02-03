# Three-sort in the textbook: Compose a program that accepts three integers from the command line and writes them in ascending order. Use the built-in min() and max() functions. (Do not use an IF statement).
import sys
import stdio

# args = sys.argv # assign the args to a variable
# args = args[1:] # remove the program_name from the list
# args = [float(i) for i in args if i.isdigit()]
# args.sort()     # sort it in ascending order

# # NOW PRINT IT
# args = [str(i) for i in args]
# stdio.write(f"{", ".join(args)}\n")

# The method if I'm forced to use min and max without an if statement
# I don't like this
# Wait is this how some sorting algorithms work, take sets of three values then sort them manually, until the whole list is sorted?
args = sys.argv # assign the args to a variable
args = args[1:] # remove the program_name from the list
args = [float(i) for i in args if i.isdigit()] # Convert each item to float
max_value = max(args)
min_value = min(args)
remove_max = args.remove(max_value)
remove_min = args.remove(min_value)
middle_value = args[0]
stdio.write(f"{min_value}, {middle_value}, {max_value}\n")
