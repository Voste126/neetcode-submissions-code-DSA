from typing import List

def read_integers() -> List[int]:
    myinput = input()
    newlist =[]
    strings = myinput.split(",")

    for s in strings:
        newlist.append(int(s))
    return newlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
