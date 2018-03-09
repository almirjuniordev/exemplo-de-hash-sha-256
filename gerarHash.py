import hashlib

palavra = input('Informe a chava que deseja criptografar: ')

palavra_sha256 = hashlib.sha256(palavra.encode('utf-8'))

print('Palavra Original: ', palavra)
print('Hash Criptografado:', palavra_sha256.hexdigest())