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

amounts = {
    "trim": perimeter,
    "paint": (wall_area + floor_area) / 350, #assuming 350 sq ft per gallon of paint
    "carpet": floor_area,
}

prices = {
    "trim": 3, #$/ft
    "paint": 20, #$/gallon
    "carpet": 30, #$/sq ft
}

estimates = {}

total = 0
for key in amounts:
    estimates[key] = prices[key]*amounts[key]
    print key.upper() + " estimate: $" + str(estimates[key])
    total = total + estimates[key]

print "Total estimated cost: $" +str(total)
