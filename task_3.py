#!/usr/bin/env python3

while True:
    # Setting input string as a lowercase to avoid case sensetivity
    usr_input = input("Type anything:\n").lower()
    if usr_input == "cancel":
        break
    else:
        digit = ''
        digits_lst = []
        for i in range(len(usr_input)-1):
            # Using sliding two-characters frame to switch between cases
            frame = (usr_input[i], usr_input[i+1])

            if i == len(usr_input)-2: # If last frame
                # Remove non-digit and non-minus-sign in frame[0] if exists
                digit += frame[0] + frame[1] if frame[0].isdigit() or frame[0] == '-' else frame[1]
                digits_lst.append(digit)
            else:
                if frame[0] == '-' and frame[1].isdigit():
                    # case: minus before digit
                    digit += '-'
                elif frame[0].isdigit() and frame[1].isdigit():
                    # case: sequence of digits
                    digit += frame[0]
                elif frame[0].isdigit() and not frame[1].isdigit():
                    # case: sequence of digits is broken
                    digit += frame[0]
                    digits_lst.append(digit)
                    digit = ''

        res = sum([int(i) for i in digits_lst])
        print(res)