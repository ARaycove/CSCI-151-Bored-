import sys
import stdio
# Modified such that an amount of names can be inputted. Then formatted into a properly formatted greeting string
def print_input_names():
    my_list = []
    args = sys.argv
    num_args = len(args)-1
    for i in range(1, num_args+1):
        # Modified such that regardless of incorrect string input, names are capitilized properly
        name = sys.argv[i]
        name = name.title()
        my_list.append(name)

    my_list.reverse()
    my_list.insert(-1,"and")
    greeting_string             = ", ".join(my_list)
    extra_comma_index           = greeting_string.rfind(",")
    second_extra_comma_index    = greeting_string.find(",")
    greeting_string             = greeting_string[:extra_comma_index] + greeting_string[extra_comma_index+1:]

    stdio.write(f"Hi {greeting_string}. \n")

