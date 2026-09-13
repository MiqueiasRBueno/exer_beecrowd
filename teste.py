from os import set_inheritable
# Exercício 1

nome_usuario = str(input("Nome de usuário: "))
while True:
  senha_usuario = str(input("Senha: "))
  if senha_usuario != nome_usuario:
    break
  else:
    print("\033[31mSenha não pode ser igual ao nome do usuário!\033[m")
print("Login efetuado com sucesso!")