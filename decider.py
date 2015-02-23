import random
import time


print(" ============ THE DECISION MAKER!! ============ \n")
options = []
title = input("What do you need to make a decision on? ")
howMany = int(input("How many options are there to choose from? "))

for n in range(howMany):
    decider = input("Enter option: ")
    options.append(decider)
    
print("\nYour have entered " +str(howMany) + " choices. Your options for ",title," are: "+", ".join(options))
print("It has been decided! \nYou will have...")
time.sleep(1)
print(random.choice(options)+"!")

