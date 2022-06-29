# this is a short Python script on string concatenation
# how strings are displayed by manipulating strings

fruit = input("What's your best fruit? ")
food = input("What food do you like the most? ")

# step 1
print("My best fruit is " + fruit + " and I love eating " + food)

# step 2
print("My best fruit is {} and I love eating {}".format(fruit, food))

# step 3
print(f"My best fruit is {fruit} and I love eating {food}")
