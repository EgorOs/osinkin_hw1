#!/usr/bin/env python3

while True:
    # Setting input string as a lowercase to avoid case sensetivity
    usr_input = input("Type anything:\n").lower()
    if usr_input == "cancel":
        break
    else:
        digits_lst = [0]
        characters = list(usr_input)
        prev_char = None
        while characters:
            ch = characters.pop(0)
            if ch.isdigit():
                sign = -1 if prev_char == '-' else 1
                digits_lst[-1] = digits_lst[-1]*10 + sign * int(ch)
            else:
                if digits_lst[-1] != 0:
                    digits_lst.append(0)
                prev_char = ch
        result = sum(digits_lst)
        print(result)

