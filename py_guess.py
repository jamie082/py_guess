#!/usr/bin/python3

from sys import argv

script, filename = argv

def enter_function():
    while True:
        print("Entered enter_function()")

digit_0 = 0
digit_1 = 1

my_list = ['Pythone', 'C++', 'Javascript']

print("argv val is output text file to create for text file\ninput 5 to write to text file")

while True:
    print("Opening the file...")
    target = open(filename, 'w')

    age = int(input("Input 0 or 1: "))

    if age == 1:
        print("One")

    elif age == 0:
        print("Zero")
    
    elif age == 5:
        enter_function()
        break
    else:
        print("Incorrect value")

print ("Good bye!")
target.close()
