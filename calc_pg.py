ligado = True

while ligado == True:
    
    # Decisão de cálculo

    print('As opções são: ultimo termo, primeiro termo, numero do termo, razao. (Digite exatamente como aparecem.) ')
   
    print('Qual tipo de calculo você quer fazer?')

    tipoDeCalculo = input()
    
    print()
    
    

    if tipoDeCalculo == 'ultimo termo':
        
        print('Insira os dados sem espaço.')

        # Recebendo
        
        print('Primeiro termo:')
        print()
        primeiroTermo = float(input())

        print('Número do último termo:')
        print()
        numTermo = float(input())

        print('Razão:')
        print()
        razao = float(input())
        
        # Processando

        resultado = primeiroTermo + ((numTermo - 1) * razao)
        
        print(f'O último termo é: {resultado}')

    elif tipoDeCalculo == 'primeiro termo':
        
        print('Insira os dados sem espaço:')

        # Recebendo

        print('Ultimo termo:')
        print()
        ultimoTermo = float(input())

        print('Numero do ultimo termo:')
        print()
        numTermo = float(input())

        print('Razão')
        print()
        razao = float(input())

        # Processando
        
        resultado = -1 * (-ultimoTermo + ((numTermo-1) * razao))

        print(f'O primeiro termo é: {resultado}')

    elif tipoDeCalculo == 'numero do termo':
        
        print('Insira os valores sem espaço:')

        # Recebendo
        
        print('Ultimo termo')
        print()
        ultimoTermo = float(input())

        print('Primeiro termo:')
        print()
        primeiroTermo = float(input())

        print('Razão')
        print()
        razao = float(input())

        # Processando
        
        resultado = (razao + ultimoTermo - primeiroTermo)/razao

        print(f'O número do termo é: {resultado}')
    
    elif tipoDeCalculo == 'razao':
        
        print('Insira os dados sem espaço:')

        # Recebendo
        
        print('Primeiro termo:')
        print()
        primeiroTermo = float(input())

        print('Ultimo termo')
        print()
        ultimoTermo = float(input())
        
        print('Numero do termo:')
        print()
        numTermo = float(input())

        # Processando
        
        resultado = (ultimoTermo - primeiroTermo)/(numTermo - 1)

        print(f'A razão é: {resultado}')
    
    else:
        
        print('digite de novo')        