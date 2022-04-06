#!/usr/bin/python3

from sys import argv
import random

script, filename = argv

def enter_function():
    print("Enter text to write: ")

    line1 = input("line 1: ")

    print("I'm going to write these to the file.")

    target.write(line1)

    print("And finally, we close it.")
    print(random.randrange(1,10))
    target.close()
    return

digit_0 = 0
digit_1 = 1

my_list = ['Python', 'C++', 'Javascript']

print("argv val is output text file to create for text file\ninput 5 to write to text file")

while True:
    # print("Opening the file...")
    target = open(filename, 'w')
    
    my_string = "Input 0 or 1 or 2 or 3"

    age = int(input(my_string)) # my_string == formatted string

    if age == 0:
        print("Zero")

    elif age == 1:
        print("One")

    elif age == 2:
        print("Two")

    elif age == 3:
        print("Three")

    elif age == 5:
        enter_function()
        break

    else:
        print("Incorrect value")

print("Good bye!")

