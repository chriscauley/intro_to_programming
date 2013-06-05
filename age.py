#age = raw_input("how old?")
#age = int(age)
my_age = 29

for age in range(19,39):
  print "age is "+str(age)
  if age == my_age:
    print "same age"
  elif age > my_age:
    print "you're old"
  else:
    print 'young'
