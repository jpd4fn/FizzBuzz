for i in range(1, 101):
    DivBy3 = i % 3 == 0
    DivBy5 = i % 5 == 0
    if DivBy3 and DivBy5:
        print("FizzBuzz")
    elif DivBy3:
        print("Fizz")
    elif DivBy5:
        print("Buzz")
    else:
        print(i)