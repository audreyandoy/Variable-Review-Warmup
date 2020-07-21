#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# ○ Use 2 variables in accepting the names (one for the first name and another for the last name).

# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# print("Hello " + last_name + " " + first_name )

# Create a for loop that will increase a counter variable by once

counter = 0
for i in range(3):
  counter += 1
  print(counter)

# Create a for loop that loops for 20 times, inside of it, do a if/else statement that will check if the loop variable is greater or less than 10.

for x in range(20):
  if x > 10:
    print("greater than", x)
  elif x == 10:
    print("x is 10", x)
  else:
    print("less than 10", x)
