
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
while Nota1 > 10 or Nota1 < 0:
    Nota1 = int(input ('Você digitou a nota errada, corrija a nota 1 = '))
Nota2 = int (input ('Nota 2: '))
while Nota2 > 10 or Nota2 < 0:
    Nota2 = int(input ('Você digitou a nota errada, corrija a nota 2 = '))
Nota3 = int (input ('Nota 3: '))
while Nota3 > 10 or Nota3 < 0:
    Nota3 = int(input ('Você digitou a nota errada, corrija a nota 3 = '))
Nota4 = int (input ('Nota 4: '))
while Nota4 > 10 or Nota4 < 0:
    Nota4 = int(input ('Você digitou a nota errada, corrija a nota 4 = '))

media = (Nota1 + Nota2 + Nota3 + Nota4) /4

print ('Media: {}' .format(media))
# if Nota1 <= 10 and Nota2 <= 10 and Nota3 <= 10 and Nota4 <= 10:
#     print ('Sua média final é = {}' .format(media))
# else:
#     print ('Alguma nota digita está incorreta!')
