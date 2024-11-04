name = "Bota"
age = 32

mess1 = "My name " + name + str (age) + " old"
print(mess1)

mess2 = "My name {} and {} old ".format(name, age)
print(mess2)

mess3 = f"My name {name} and {age} old"
print(mess3)

print (f"My name {name.upper()} and {age} old")
