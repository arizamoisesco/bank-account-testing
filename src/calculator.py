def sum(a,b):
    """
    >>> sum(5,7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b

def substract(a, b):
    '''
    >>> substract(10,5)
    5
    '''
    return a - b

def multiply(a,b):
    '''
    >>> multiply(2,5)    
    10
    '''
    return a * b

def divide(a , b):
    '''
    >>> divide(10,0)
    'No se puede dividir por cero'
    '''

    try: 
        resultado = a / b
    except ZeroDivisionError:
        resultado = "No se puede dividir por cero"

    return resultado