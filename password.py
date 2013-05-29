guesses = 0
knows_password = False
while guesses < 3:
    password = raw_input("What is the password: ")
    if password == "Rumplestiltskin":
        print "That's correct!"
        knows_password = True
        break
    if len(password) == 0:
        # They didn't enter anything, don't hold it against him
        print "You didn't enter anything."
        continue
    guesses = guesses + 1
    print "Wrong password, try again. You have " + str(3-guesses) + " guesses left."

if knows_password:
    print "Welcome!"
    # the rest of the program
else:
    print "Unathorized login attempt. This computer will self-destruct in 10 seconds."
