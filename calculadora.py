num_one = int(input('Digite o primeiro numero:'))
num_two = int(input('Digite o primeiro numero:'))
texto = input('Digite o numero da operação: 1\soma,2\div,3\sub,4\multi')
div = num_one / num_two
sub = num_one - num_two
soma = num_one + num_two
multi = num_one * num_two
if texto == '1':
   print('O resultado da soma é',soma)
elif texto == '2':
   print('O resultado da divisão é',div)
elif texto == '3':
   print('O resultado da subtração é',sub)
elif texto == '4':
   print('O resultado da multiplicação é',multi) 
