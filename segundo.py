

# foi a unica forma que consegui fazer as distância. 
print( "-"   *4,'bem-vindo a pizzaria do João Batista Leon Campos' ,'-'*4,) 
print( "-" *24,'cardápio' ,'-'*24,)
print( '-'*58,)
print('-'*4,'|', 'Tamanho' ,'|' , 'Pizza Salgada(PS)', '|', 'Pizza Doce(PD)','|','-'*4)
print('-'*4,'|  ','P    ' ,'|    ' ,  'R$ 30.00     ' , '|  ', 'R$ 34,00'  , '    |','-'*4)
print('-'*4,'|  ', 'M    ','|    ' ,  'R$ 45.00     ' , '|  ','R$ 48,00' ,  '    |','-'*4)
print('-'*4,'|  ', 'G    ','|    ' ,  'R$ 60.00     ' , '|  ','R$ 66,00' ,  '    |','-'*4)
print( '-'*58,)


valor = 0 # variável pra pedido saldado.
money =0  # variável pedido doce.
valor_total=0
while True:  
    
    sabor = input(" \n Entre com o sabor desejado (PS/PD): ").upper() # fiz mais uma variável pra não voltar nesse laço de repetição.
    if sabor not in ['PS', 'PD']:
        print(" Sabor inválido. Tente novamente")
        continue  
    

    
    tamanho = input(" Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("  Tamanho inválido. Tente novamente")
        continue   
    
    
    if sabor == 'PS':
        if tamanho == 'P':
            preco = 30.00
        elif tamanho == 'M':
            preco = 45.00
        elif tamanho == 'G':
            preco = 60.00
        valor  += preco    
        print(f' voce pediu pizza salgada : R${valor} ') 
   
    elif sabor == 'PD':
        if tamanho == 'P':
            preco = 34.00
        elif tamanho == 'M':
            preco = 48.00
        elif tamanho == 'G':
            preco = 66.00
        money  += preco    
        print(f' voce pediu pizza doce : R${money} ')
       
    valor_total += preco # variável pra somar valores .

    mais_alguma = input(" \n Deseja  mais alguma coisa? (S/N): ").upper()
    if mais_alguma == 'S':
        continue  # apertar "S" continua o pedido.

    if mais_alguma == 'S':
        break  # aqui do break é no caso de encerrar , ele encerra com qualquer outra letra que não seja o "S".
    print(f'      \n  O Valor total a ser pago: R${valor_total} ')
     
     # pra não voltar novamente fiz uma variável pra encerra aqui , mas gotaria de que o corretor comentasse sobre.
    encerrar= input("      obrigado pela prefência")
       
