def calcular_par_impar(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    result = soma%2
    par_impar = ''
    if result == 0:
        par_impar = 'Par'
    elif result == 1:
        par_impar = 'Ímpar'

    return par_impar