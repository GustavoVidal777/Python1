a = int (input('Digite valor A: '))
b = int (input('Digite valor B: '))
soma = a + b
sub = a - b
multi = a * b
div = a / b 
resto = a % b 
print ('soma = {}. \nsubtração = {}. \nmultiplicação = {}. \ndivisão = {}. \nresto = {}.' .format (soma, sub, multi, div, resto))
# acima concatenação geral usando format
print ('Soma = ' + str(soma))
print ('Subtração = ' + str(sub))
print ('Multiplicação = ' + str(multi))
print ('Divisão = ' + str(div))
print ('Resto = ' + str (resto))


