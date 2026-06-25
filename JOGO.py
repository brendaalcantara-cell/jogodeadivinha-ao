import random
print(**********************************)
print("Bem vindo ao jogo de Adivinhação")
print(**********************************)

numero_secreto= random.randrange(1, 51)
totaldetentativas= 10

chute=input("Digite o seu número:")
print ("você digitou: ",chute )

chutenumerico= int (chute)

while(totaldetentativas > 0):
    print("Você tem", totaldetentativas,"tentativas")
   
    print("Tentativa restante:", totaldetentativas)
   

    if(totaldetentativas== 0):
        print("Voce não tem mais tentativas. Fim do jogo.")
        break


acertou= chuteNumerico== numero_secreto
maior=chutenumerico> numero_secreto
menor=chutenumerico<numero_secreto


# se voce digitar qualquer número vou verificar se acertou ou errou
if(acertou):
    print("Parabéns! Você acertou! Fim de jogo")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
        
     totaldetentativas= totaldetentativas - 1 
    print("fim do jogo")
