from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    # last three elements of any list
    # REVERSE elements of any list
    last_list = my_list[::-1]
    for n in range(len(last_list)):
        newlist = last_list[0:3]
        return newlist[::-1]

    


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
