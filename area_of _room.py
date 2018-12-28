'''Exercise 3: Area of a Room
(Solved—13 Lines)
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
'''


# ask the user to enter the width  of a room as floating number ==> input
width = float(input('Enter your room with in meters : '))
# asks the user to enter the  length  of a room as floating number ==> input
length = float(input('Enter your room length in meters :'))
# compute the area of the room  area =  width x length ==> processing
Area = width * length
# display the compute including meters unit ==> output
print('Your room Area is {} meters '.format(Area))
