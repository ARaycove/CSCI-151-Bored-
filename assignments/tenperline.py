# Compose a filter tenperline.py that reads a sequence of integers between 0 and 99 and writes 10 integers per line, with columns aligned.


# > python randomintseq.py 100 50 | python tenperline.py
#     0   86    1   31   93   90   16    1   75   35
#     1   13   98   42   81   85   81   96   12   53
#    69   89    5   63   19   22   68   51   46   71
#    94   21   23   99   87    8   69   37   61   76
#    98   11   93   41   88   33   30   35   96   39

##############################################
#
# Header 
# Aaron Raycove
# 02/14/2025
#
##############################################
import stdio

# Loop variable now!
counter = 0

while not stdio.isEmpty():
    # Read as int
    value = stdio.readInt()
    # write the filtered value
    stdio.write(f"{value:^5}")
    # Increment the timer
    counter += 1
    # If the counter hits 10, write a newline character
    if counter >= 10:
        stdio.writeln()
        counter = 0

# Final newline character once we break the loop
stdio.writeln()