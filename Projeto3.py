
# x = int (input ('Primeiro valor: '))
# y = int (input ('Segundo valor: '))
# z = int (input ('Segundo valor: '))
# if x > y and x > z:
#         print ('O maior número é {}' .format(x))
# elif y > x and y > z:
#         print ('O maior número é {}' .format(y))
# else:
#         print ('O maior número é {}' .format(z)) 

# a = int (input ('Primeiro valor: '))
# b = int (input ('Primeiro valor: '))
# resto_a = a % 2
# resto_b = a % 2

# if resto_a == 0 or not resto_b > 0:
#     print ('Digitado 1 Numéro par!')
# else:
#     print ('Nenhum número par foi digitado!')

Nota1 = int (input ('Nota 1: '))
Nota2 = int (input ('Nota 2: '))
Nota3 = int (input ('Nota 3: '))
Nota4 = int (input ('Nota 4: '))

media = (Nota1 + Nota2 + Nota3 + Nota4) /4

if media >= 7:
    print ('Parabéns você foi aprovado com média: {}' .format(media))
elif media >= 6:
    print ('Sua média foi {} , está de recuperação' .format(media))
else:
    print ('Infelizmente sua média foi {} você foi reprovado ' .format(media))