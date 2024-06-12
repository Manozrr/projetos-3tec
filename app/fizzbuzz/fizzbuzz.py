def fizzbuzz(num:int):
    #Retorna "fizz" se num é divisivel por 3
    if num % 3 == 0 and num % 5 ==0:
        return 'fizzbuzz'
    #Retorna "buzz" se num é divisivel por 5
    elif num % 3 == 0:
        return 'fizz'
    #Retorna "fizzbuzz" se num é divisivel por 15
    elif num % 5 == 0:
        return 'buzz'
    #Retorna o número se num não for divisivel por 3
    else:
     return num