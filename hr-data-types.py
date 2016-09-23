#! /usr/bin/env python3

i = 4
d = 4.0
s = 'Hacker Rank '

# Declare second integer, double, and String variables.
int_input = 0
float_input = 0.0
str_input = ''

# Read and save an integer, double, and String to your variables.
int_input = int(input().strip())

float_input = float(input().strip())

str_input = input().strip()

# Print the sum of both integer variables on a new line.
print(i + int_input)

# Print the sum of the double variables on a new line.
print("%.1f" % (d + float_input))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + str_input)
