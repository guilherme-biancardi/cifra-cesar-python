from modules.CifraCesar import CifraCesar

index = int(input('digite a chave da cifra: '))

crypt = CifraCesar(index)
print(crypt.encryptMessage(input('digite uma mensagem: ')))
question = input('deseja descriptografar a mensagem agora? (s/n): ')

if(question == 's'):
    crypt.decryptMessage()
    print(crypt.getMessage())
else:
    print('fim de execução')