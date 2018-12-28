'''
Exercise 4: Area of a Field
(Solved—15 Lines)
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
'''

# ask the user to enter the width  of a room  ==> input
width = float(input('Enter the width of your room in feet :'))
# ask the user to enter the length  of a room  ==> input
length = float(input('Enter the length of your room in feet :'))
# compute the area area = width * length / 43560==> processing
area_in_acres = width * length / 43560

# Display the area in acre  == > output
print('your area in acre is  {} '.format(area_in_acres))
