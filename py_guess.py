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
    target.close()
    return

digit_0 = 0
digit_1 = 1

my_list = ['Python', 'C++', 'Javascript']
list = ['Press 0', 'or 1', 'or 2', 'or 3']

print("argv val is output text file to create for text file\ninput 5 to write to text file")

while True:
    # print("Opening the file...")
    target = open(filename, 'w')
    
    my_string = list

    age = int(input(my_string)) # my_string == formatted string

    if age == 0:
        print("Zero")

    elif age == 1: 
        print("One")
        while 'Press 0' in list:
            list.remove('Input 0')

    elif age == 2:
        print("Two")
        while 'or 2' in list:
            list.remove('or 2')

    elif age == 3:
        print("Three")
        while 'or 3' in list:
            list.remove('or 3')

    elif age == 5:
        enter_function()
        break

    else:
        print("Incorrect value")

print("Good bye!")

