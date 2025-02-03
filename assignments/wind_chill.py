# Problem Statement

# Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:
# w = 35.74 + 0.6215 t + (0.4275 t - 35.75) v0.16

# Compose a program that takes two floats t and v from the command-line and writes the wind chill. Note: the formula is not valid if t is larger than 50 in absolute value or if  v is larger than 120 or less than 3 (you may assume that the values you get are in that range).

# HEADER
# Solves the problem statement above
# accepts two inputs
# prints the result to the console in a formatted f string

import sys
import stdio

def calc_wind_chill():
    # Define our variables and convert them
    temperature = float(sys.argv[1])
    wind_speed = float(sys.argv[2])
    # Throw an error message if the input is not valid (not part of assignment but here we go)
    if (abs(temperature) > 50) or ((wind_speed > 120) or (wind_speed < 3)):
        return "Invalid Input\n"
    
    # Run the calculation based on the inputs
    wind_chill = 35.74 + (0.6215 * temperature) + (((0.4275*temperature)-35.75) * (wind_speed ** 0.16))

    # Construct a string to print the output to the console
    string_one = f"Temperature = {temperature}\n"
    string_ond = f"Wind Speed  = {wind_speed}\n"
    string_onf = f"Wind Chill  = {wind_chill}\n"
    formatted_output = string_one + string_ond + string_onf

    # This is a return statement, WOW!
    return formatted_output


# Get the Result of the calculation
result = calc_wind_chill()
# Print the result, rolls off the tongue better than stdio.write the result.
stdio.write(result)