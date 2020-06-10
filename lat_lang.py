from math import *

#You need Radius of earth to find the distance between two points
radius_of_earth = 6373.0

# You can use the simple .split(" ") with float to get input but this is fast trick called 'List Comprehension'

my_long, my_lat = [float(my_long) for my_long in input('Enter you location longitude and latitude with space between them: ').split()]
desired_long, desired_lat = [float(desired_long) for desired_long in input('Enter you location longitude and latitude with space between them: ').split()]

# Radians are used because the points are in float value

longitude = radians(desired_long) - radians(my_long)
latitude = radians(desired_lat) - radians(my_lat)

#Net se mila tha ye formula

formula = sin(latitude/ 2)**2 + cos(my_lat) * cos(desired_lat) * sin(longitude/ 2)**2
another_formula = 2 * atan2(sqrt(formula), sqrt(1 - formula))

distance = radius_of_earth * another_formula
# ta- da !!
print(distance)


