length = raw_input("What is the length of the room?")
length = int(length)
width = raw_input("What is the width of the room?")
width = int(width)  
height = raw_input("What is the height of the room?")
height = int(height)

perimeter = 2 * int(length) + 2 * int(width)
wall_area = perimeter * int(height)
floor_area = length * width # also the ceiling_area!

amount_of_trim = perimeter
amount_of_paint = (wall_area + floor_area) / 350 #assuming 350 sq ft per gallon of paint
amount_of_carpet = floor_area

price_of_trim = 3 #$/ft
price_of_paint = 20 #$/gallon
price_of_carpet = 30 #$/sq ft

trim_estimate = price_of_trim * amount_of_trim
paint_estimate = price_of_paint * amount_of_paint
carpet_estimate = price_of_carpet * amount_of_carpet

print "Trim estimate: $" + str(trim_estimate)
print "Print estimate: $" + str(paint_estimate)
print "Carpet estimate: $" + str(carpet_estimate)
print "Total estimated cost: $" + str(trim_estimate+paint_estimate+carpet_estimate)
