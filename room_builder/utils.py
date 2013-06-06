def curse_zues():
    print "Zues, why have you abandoned me!!!"

def greet_user(name):
    print "Hello, "+name+". It is good to see you again."

def add3(number1,number2,number3):
    return number1 + number2 + number3

def first_greater_than_5(some_list):
    for i in some_list:
        if i > 5:
             return i

def number_input(question):
    """ Just like raw_input, but forces a number and returns an integer """
    while True:
        input = raw_input(question)
        if input.isdigit():
            break
        else:
            print "Invalid input. Please enter a number."
    return int(input)

def dict_input(options,question):
    """ Just like raw_input, only it only accepts options printed from a dict """
    num_options = len(options)
    i = 1
    print question
    for option in options:
        print str(i) + "-" + option
        i = i+1
    while True:
        answer = raw_input("Select an option (1-"+str(num_options)+"): ")
        if answer.is_digit():
            if int(answer) > 0 and int(answer) <= num_options:
                return options[int(answer)]

def get_room():
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
        "wall_sockets": perimeter/15, #Q1
        }
    return amounts

def price_room(room,print_prices):
    prices = {
        "trim": 3, #$/ft
        "paint": 20, #$/gallon
        "carpet": 30, #$/sq ft
        "wall_sockets": 40 #$/socket, #Q1
        }
    
    estimates = {}
    
    total = 0
    for key in room:
        estimates[key] = prices[key]*room[key]
        if print_prices:
            print key.upper() + " estimate: $" + str(estimates[key])
        total = total + estimates[key]
    return total
