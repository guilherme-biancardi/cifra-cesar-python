from modules.letters import Letters
from modules.CifraCesar import CifraCesar

index = int(input('digite o indexador da cifra: '))
crypt = CifraCesar(index, Letters())

print(crypt.encryptMessage(input('digite uma mensagem: ')))
