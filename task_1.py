#!/usr/bin/env python3

usr_input = input("Type anything:\n").split()

# The solution below doesn't preserve the original order of elements on Python 3.5.2
# unique_instances = set(usr_input)
# res = ''.join([str(i)+' ' for i in unique_instances]) 

# This solution returns elements in the original order
unique_instances = []
for i in usr_input:
    if i not in unique_instances:
        unique_instances.append(i)

res = ' '.join(unique_instances)
print(res)
