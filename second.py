for i in range(1,100):
    #Divided by 3 and 5 = FizzBuzz
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    #Divided by only 5 = Buzz
    elif i%5==0:
        print("Buzz")


    #Divided by only 3 = Fizz
    elif i%3==0:
        print("Fizz")

    print(i)