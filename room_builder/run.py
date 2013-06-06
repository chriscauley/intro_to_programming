from utils import get_room, price_room

enter_room = 'y'
rooms = []

while True:
    if enter_room == 'y':
        rooms.append(get_room())
    elif enter_room == 'n':
        break
    else: 
        print "Invalid input, try again."
    enter_room = raw_input("Would you like to enter another room? (y/n) ")

total = 0
for room in rooms:
    total = total + price_room(room,False)

print "Final total: $"+str(total)
