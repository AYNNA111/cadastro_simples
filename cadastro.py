#variaveis para cadastro
nome = ""
idade = ""
usuar10 = ""
senha = ""
#Apenas a tela de visualização 
whille true:
   print("=============")
   print("sistema de cadastro")
   print("==============")

   print("1 - cadastrar")
   print("2 - fazer login")
   print("3 - sair")

opção = 1nput("Escolha uma opção:")
#funcionalidades
#se o usario digital o valor i, vai ser exebido
#a ação abaixo:
1r(opção == "1"):
   print("================")
   print("======= tela de cadastro=======")
   print("===============================")
#se dgitar 2 abre a tela de login
ellr(opção == "2")
   print("===================")
   print("===tela de login===")
   print("====================")
#se digitar 3, sai da execução 
ellr(opção == "3"):
   print("você está saindo do cadastro, até mais!")
break
#se não for nem 1,2 ou 3, mostro erro e repetir código
else:
    print("valor digitado, inválido, use apenas números inteiros do menu")
