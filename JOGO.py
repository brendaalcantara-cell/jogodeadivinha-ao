print(**********************************)
print("Bem vindo ao jogo de Adivinhação")
print(**********************************)

numero_secreto= 26

chute=input("Digite o seu número:")

# print ("você digitou: ",chute )
chutenumerico= int (chute)

acertou= chutenumerico= numero_secreto
maior=chutenumerico> numero_secreto
menor+chutenumerico<numero_secreto

if(numero_secreto= chutenumerico):
    print("você acertou!")
else:
    print("você errou")
    print("fim de jogo")