import sys
import stdio
args = sys.argv # assign the args to a variable
args = args[1:] # remove the program_name from the list
args = [float(i) for i in args if i.isdigit()] # Convert each item to float
condition = True
while condition:
    if args[0] > args[1]:
        args = [args[1], args[0], args[2]]
    if args[1] > args[2]:
        args = [args[0], args[2], args[1]]
    if args[2] >= args[0] and args[2] >= args[0]:
        if args[1] > args[0]:
            condition = False
stdio.write(f"{args}\n")