#!/usr/bin/python3
for letter in range(65, 90):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
