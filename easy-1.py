#!/usr/bin/env python3

'''
create a program that will ask the users name, age, and reddit
username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is
(blank)

for extra credit, have the program log this information in a file to
be accessed later.

'''

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    username = input("Enter your username: ")
    print("your name is %s, you are %s years old and your username is %s" %
          (name, age, username))

    with open('easy-1.txt', 'w') as f:
        f.write("your name is %s, you are %s years old and your username is %s" %
                (name, age, username))
