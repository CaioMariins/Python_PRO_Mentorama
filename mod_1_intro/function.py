def check_n(n_n):
    """Retorna a frase correspondente ao número."""
    if (n_n % 5 == 0) and (n_n % 7 == 0):
        return print("fizzbuzz"), str("fizzbuzz")
    if n_n % 7 == 0:
        return print("buzz"), str("buzz")
    if n_n % 5 == 0:
        return print("fizz"), str("fizz")
    if (n_n % 5 !=0) and (n_n % 7 !=0):
        return print("miss"), str("miss")
    return None
    