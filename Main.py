palavra_secreta = 'toalha'
letras_acertadas = ['_'] * len(palavra_secreta)
tentativas = 9 

print ('Bem vindo ao jogo da forca! ')

palavra_mostrada = ' '

while tentativas > 0 : 

    # CÓDIGO CORRETO:
    print(f'Adivinhe a palavra: {" ".join(letras_acertadas)}')
    print (f'Você ainda tem {tentativas} tentativas. ')


    chute = input('Qual letra deseja chutar ? ')

    if chute in palavra_secreta :  
        print ('Você acertou! ')

        for indice, letra in enumerate(palavra_secreta) : 
            if chute == letra : 
                letras_acertadas[indice] = letra

    else : 
        tentativas -= 1 
        print ('Você errou! Tente novamente! ')
        print (f'Você ainda tem {tentativas} tentativas. ')

    if "_" not in letras_acertadas : 
        print (f'Você ganhou! A palavra era {palavra_secreta}  ')
        break
   

    

        
        
