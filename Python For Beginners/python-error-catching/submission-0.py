def divide_numbers(a: str, b: str) -> None:
    
    try:
        input1= int(a)
        input2= int(b)
        result = input1/input2
        print(result)
    except Exception as error:
        print("An error occurred:", error)
        



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
