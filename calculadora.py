num_one = int(input('Digite o primeiro numero:'))
num_two = int(input('Digite o primeiro numero:'))
texto = input('Digite o numero da operação: 1\soma,2\div,3\sub,4\multi')
div = num_one / num_two
sub = num_one - num_two
soma = num_one + num_two
multi = num_one * num_two
if texto == '1':
   print(soma)
elif texto == '2':
   print(div)
elif texto == '3':
   print(sub)
elif texto == '4':
   print(multi) 
