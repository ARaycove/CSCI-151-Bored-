# The barcode used by the U.S. Postal System to route mail is defined as follows:  Each decimal digit in the ZIP code is encoded using a sequence of three half-height and two full-height bars.  The barcode starts and ends with a full-height bar (the guard rail) and includes a checksum digit (after the five-digit ZIP code or ZIP + 4), computed by summing up the original digits modulo 10.  

# Define the following functions:

 

#     Draw a half-height or full-height bar on stddraw.
#     Given a digit, draw its sequence of bars.
#     Compute the checksum digit.

 

# Also define global code that read in a five- (or nine-) digit ZIP code as the command-line argument and draws the corresponding postal barcode. 
# checksum = ∑digits % 10

#################################
# barcode!
# By Aaron Raycove
# 03/10/2025
#################################
# These are import statements!
import stdarray
import stdio
import sys
import stddraw

# Binary string representation of bar codes, index is digit
bar_codes = stdarray.create1D(10, 0)
bar_codes[1] = "00011"
bar_codes[2] = "00101"
bar_codes[3] = "00110"
bar_codes[4] = "01001"
bar_codes[5] = "01010"
bar_codes[6] = "01100"
bar_codes[7] = "10001"
bar_codes[8] = "10010"
bar_codes[9] = "10100"
bar_codes[0] = "11000"
#############
def calc_checksum(zip_code):
    '''
    Calculates the checksum digit (sum of digits in zip code module 10)
    '''
    # As per instructions checksum is sum of digits modulo 10
    # I looked up how actual checksums are calculated, and woah is that complicated for no reason
    return sum([int(i) for i in zip_code])%10  

def draw_bar(n: int, x_pos: float | int):
    '''
    takes argument 0 or 1 and draws a singular bar at x_pos,
    Draws a single bar of height n at x_pos
    '''
    #############
    # type conversion
    n = int(n)
    # ensure its a 0 or 1 being inputted
    if n != 0 and n != 1:
        raise Exception("Argument n must be 0 or 1")
    # Constants
    FULL_HEIGHT = 0.25
    HALF_HEIGHT = 0.5
    height_of_bar = None
    # based on binary input, set the height of the bar to be drawn
    if n == 0:
        height_of_bar = HALF_HEIGHT
    elif n == 1:
        height_of_bar = FULL_HEIGHT
    # Now draw the actual bar
    stddraw.filledRectangle(x_pos, 0, 0.025, height_of_bar)

def draw_barcode(zip_code: int):
    '''
    takes a 5 or 9 digit zip_code and draws a corresponding bar code
    '''
    #############
    # Zipcode should be 5 or 9, so verify and get total number of positions based on zip_code
    r = 2
    bars = len(str(zip_code))
    total = r + (bars*5) # times 5 becomes each digit has 5 bars
    if bars != 5 and bars != 9:
        raise Exception("must be 5 or 9 digit zipcode")
    # declare the bar code positions
    positions = stdarray.create1D(total, 0)
    for i in range(total):
        positions[i] = (0.05 * i) + 0.005
    # Set the x scale accordingly
    stddraw.setXscale(0, positions[-1]+0.025)

    #############
    # Get full string representation of entire barcode
    binary_rep = ""
    zip_code = str(zip_code)
    for i in zip_code:
        binary_rep += bar_codes[int(i)]

    #############
    draw_bar(0, 0.005) # draw front guardrail
    # Iterate over the binary representation and draw the entire bar_code
    for x_pos, bit in enumerate(binary_rep):
        draw_bar(int(bit), positions[x_pos+1])
    draw_bar(0, positions[-1]) # draw rear guardrail
    # Print the checksum on the image
    stddraw.text(0.5, 0.75, f"Checksum: {str(calc_checksum(zip_code))}")
    # Display to user
    stddraw.show()

if __name__ == "__main__":
    # Collect input
    zip_code = sys.argv[1]
    zip_code = int(zip_code)
    # Call main function
    draw_barcode(zip_code=zip_code)
    