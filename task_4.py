#!/usr/bin/env python3


while True:
    usr_input = input("Type anything:\n")
    if usr_input == "cancel":
        break
    else:
        min_val = 1
        unique_values = set(usr_input.split(' '))
        while True:
            if str(min_val) in unique_values:
                print(unique_values)
                min_val += 1
            else:
                break
        print(min_val)
