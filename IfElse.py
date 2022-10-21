#Condição If = estrutura condicional que executa uma linha de código se for verdadeira, ou 'true'
idade = int(input("Qual a tua idade?: "))

if idade >= 18: #if representa um "se", neste caso, se idade for maior ou igual a 18..
    print("Você é um adulto")
elif idade == 100: 
   print("Você tem um século de idade, tu é véi hein!!!")
elif idade < 0: #elif representa elseif, se o if de cima resultar em falso, pula pro elif, se o elif tambem for falso, executará o else
   print("Você ainda nem nasceu")
else: #else representa a outra saída, no caso um dado falso, se o dado inserido não condiz com o programa
    print("Você é menor de idade")

== igual a
>= maior ou igual a
<= menor ou igual a
< menor que
>maior que
!= diferente
'---------------------------------------------------------------------------------------------------'
num_2 = 4

if num_1 == num_2:
    print(num_1 ** num_2) #se numero 1 for igual a 2, num 1 elevado a num 2
else: #senão
    print(num_1 * num_2) #num1 multiplica por num2

'---------------------------------------------------------------------------------------------------'
#OPERADORES RELACIONAIS


user  = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

user_bd = 'Pedrucs'
senha_bd = '123456'

if user_bd == user and senha_bd == senha:
    print('Você está logado, bem vindo')
else:
    print('Usuário ou senha inválidos.')

