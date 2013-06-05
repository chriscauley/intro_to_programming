import datetime as dt # a nice trick to save characters and to avoid confusion.

my_birthday = dt.datetime(1983,6,20) #June 20,1983
now = dt.datetime.now()

my_age = now-my_birthday # a timedelta object

print "I am " + str(my_age.days/365) + " years and " + str(my_age.days%365) + " days old."

#how many days are in a billion seconds?
num_days = 1000000000 / (60*60*25)
datetime_billion = dt.timedelta(num_days) + my_birthday
print "I'll be a billion seconds old on " + str(datetime_billion)
days_to_billion = (datetime_billion - dt.datetime.now()).days
print "That is in " + str(days_to_billion) + "days"
