for numbers in range(0,31):
    if numbers%3 == 0 and numbers%5 == 0:
        print("Fizz Buzz")
    elif numbers%3 == 0:
        print("Fizz")
    elif numbers%5 == 0:
        print("Buzz")
    else:
        print (numbers)
        
    