def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_odd(number):
    return not is_even(number)

def is_any_odd(some_list):
    for i in some_list:
        if is_odd(i):
            return True
    return False

def check_sum(some_string,digit):
    total = 0
    for character in some_string:
        if character.isdigit():
            total = total + int(character)
    if total % digit == 0:
        return True
    return False

print check_sum('1213fsr',6)
