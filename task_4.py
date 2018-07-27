#!/usr/bin/env python3

while True:
    # Setting input string as a lowercase to avoid case sensetivity
    usr_input = input("Type anything:\n")
    if usr_input == "cancel":
        break
    else:
        
    #     potential_least_positive = 1
    #     max_val = 0
    #     # sorted() is O(n*logn)
    #     for i in sorted(usr_input.split()):
    #         if int(i) == potential_least_positive:
    #             potential_least_positive += 1
    #         if int(i) > max_val:
    #             max_val = int(i)

    #     if potential_least_positive >= max_val:
    #         print('No solution: there is no skipped positive numbers.')
    #     elif max_val == 1:
    #         print('No solution: 1 is the only number in sequence.')
    #     else:
    #         print(potential_least_positive)

        max_val = 0
        N = set()
        # It seems like .split() has O(n) complexity
        for i in usr_input.split():
            if int(i)> max_val:
                max_val = int(i)
            N.add(int(i))
        # Create set of all positive numbers from least to biggest in input
        pos_nums = set(range(1,max_val+1))

        # The complexity of the part below is O(len(pos_nums)) in average case
        # accourding to the link https://wiki.python.org/moin/TimeComplexity#set
        print(list(pos_nums ^ N)[0])