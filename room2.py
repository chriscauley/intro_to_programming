def number_input(question):
    """ Just like raw_input, but forces a number and returns an integer """
    while True:
        input = raw_input(question)
        if input.isdigit():
            break
        else:
            print "Invalid input. Please enter a number."
    return int(input)

length = number_input("What is the length of the room?")
width = number_input("What is the width of the room?")
height = number_input("What is the height of the room?")

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
