def check_n(n):
    """
    O retorno duplo do print +  a string é uma solução para evitar lidar com os nones do pytest
    e ao mesmo tempo imprimir para o usuário a mensagem necessária.
    
    """

    if (n % 5 == 0) and (n % 7 == 0):
        return print("fizzbuzz"), str("fizzbuzz")
    elif (n % 7 == 0):
        return print("buzz"), str("buzz")
    elif (n % 5 == 0):
        return print("fizz"), str("fizz")
    elif (n % 5 !=0) and (n % 7 !=0):
        return print("miss"), str("miss")