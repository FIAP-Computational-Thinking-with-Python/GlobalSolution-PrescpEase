##Global solution - HAPVIDA

##Valida se o que foi digitado é um valor númerico
def numeric_input(user_input):

    while not user_input.isnumeric():
     print("A resposta precisa ser um número válido")
     user_input =  input("Escolha o tipo de usuário:\n1 - Profissionais\n2 - Pacientes\nDigite opção correspondente: ")
    
    user_type = int(user_input)
    

    return user_type
   


   


def login_type():
    print("######## Bem vindo ao sistema Prescp Ease ######## ")

    user_type = input("Escolha o tipo de usuário:\n1 - Profissionais\n2 - Pacientes\nDigite opção correspondente: ")

    numeric_input(user_type)
    
  




    

 
    

login_type()






