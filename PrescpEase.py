

##Valida se o que foi digitado é um valor númerico
def numeric_input(user_input):
    
    while not user_input.isnumeric():
     print("A resposta precisa ser um número válido")
     user_input =  input("Escolha o tipo de usuário:\n1 - Profissionais\n2 - Pacientes\nDigite opção correspondente: ")
  
     
    
    while not( user_input != "1" or user_input != "2"):
        print("A opção escolhida não é válida! Escolha entre a opção 1 e 2!")
        user_input = input("1 - Profissionais \n 2 - Pacientes\n Digite a opção: ")
        

        



   


   


def login_type():
    print("######## Bem vindo ao sistema Prescp Ease ######## ")

    user_input =  input("Escolha o tipo de usuário:\n1 - Profissionais\n2 - Pacientes\nDigite opção correspondente: ")

    numeric_input(user_input)

   
    
   


  
    

  
    
  




    

 
    

login_type()






