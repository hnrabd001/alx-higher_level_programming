#!/usr/bin/python3

for letter in range(ord('a'), ord('z)+1):
    if letter == 'q' or letter == 'e':
        continue
    print("{:c}".format(alpha_letters), end="")
