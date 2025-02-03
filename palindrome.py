import stdio
import sys
# Wrap the entire thing in a try except statement in case the user does not give an argument
try:
    # Grab the argument and assign it as a string
    my_string = str(sys.argv[1])
    orig_string = str(sys.argv[1])

    # Create the reversed string
    reverse_string = my_string[-1:0:-1] # string slice omits the last character
    reverse_string += my_string[0] # make sure we add the missing character

    # Check for equivalency if "dog" == "god" or "dod" == "dod"
    # Return the appropriate output based on result
    if reverse_string == my_string:
        stdio.write(f"{orig_string} is a Palindrome\n")
    else:
        # if it's not immediately a palindrome, we can slice out any non-alpha characters and check again
        my_string = "".join([str(i) for i in my_string if i.isalpha()])
        reverse_string = "".join([str(i) for i in reverse_string if i.isalpha()])
        # If it is now equivalent then its imperfect, else its not a palindrome
        if reverse_string == my_string:
            stdio.write(f"{orig_string} is an inexact Palindrome\n")
        else:
            stdio.write(f"{orig_string} is NOT a Palindrome\n")

except IndexError:
    # Tell the user to enter an argument if they failed to do so
    stdio.write("Please enter an argument when running palindrome.py \n")