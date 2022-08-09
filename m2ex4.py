#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def adicao(a,b):
    return(n1+n2)
def subtracao(a,b):
    return(n1-n2)
def multiplicacao(a,b):
    return(n1*n2)
def divisao(a,b):
    return(n1/n2)

def cabecalho():

  print('-' *26)
  print('    CALCULADORA BÁSICA')
  print('-' *26)
  print('''  1. Soma
  2. Subtração
  3. Multiplicação
  4. Divisão''')
  
  print('-' *26)


cabecalho() 
x = int(input('\nEscolha uma das opções citadas acima: '))
if x == 1:
  print(' ')
  print('\nOpção escolhida => SOMA: ')
elif x == 2:
  print(' ')
  print('\nOpção escolhida => SUBSTRAÇÃO: ')
elif x == 3:
  print(' ')
  print('\nOpção escolhida => MULTIPLICAÇÃO: ')
elif x == 4:
  print(' ')
  print('\nOpção escolhida => DIVISÃO: ')
elif x != 1 and x !=2 and x !=3 and x!=4:
  print('\n0. ')
  print(' ')
  exit(0)
  
n1 = float(input('\nInsira o primeiro número: \n'))
n2 = float(input('\nInsira o segundo número: \n'))

if x == 1:
    print(' \n=> Resultado da soma entre ', '(',n1, '+' ,n2,')', 'é', float(adicao(n1, n2)),'.')
if x == 2:
    print(' \n=> Resultado da subtração entre ', '(',n1, '-' ,n2,')', 'é', float(subtracao(n1, n2)),'.')
if x == 3:
    print(' \n=> Resultado da multiplicação entre ', '(',n1, '*' ,n2,')', 'é', float(multiplicacao(n1, n2)),'.')
if x == 4:
    print(' \n=> Resultado da divisão entre ', '(',n1, '/' ,n2,')', 'é', float(divisao(n1, n2)),'.')

