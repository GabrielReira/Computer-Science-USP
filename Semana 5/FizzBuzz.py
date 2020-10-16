def fizzbuzz(número):
    if (número % 3 == 0) and (número % 5 != 0):
        return 'Fizz'
    elif (número % 3 != 0) and (número % 5 == 0):
        return 'Buzz'
    elif (número % 3 == 0) and (número % 5 == 0):
        return 'FizzBuzz'
    else:
        return número