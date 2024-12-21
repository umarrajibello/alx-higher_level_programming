#!/usr/bin/python3
def uppercase(str):
    for c in str:
        cd = ord(c)
        if  cd >= 97 and cd <= 122:
            cd -= 32
        print("{:c}".format(cd), end="")
    print("")
