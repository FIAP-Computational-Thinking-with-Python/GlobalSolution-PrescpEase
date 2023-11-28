import messages


##Arrays 
options = ["1" , "2"]

professional_usernames = ["Marianaaaaa" , "Suzane" , "leonardo" , "Mariana"]
patients_usernames = ["Enzo" , "Breno" ,"André" , "Janaina"]


prescriptions = []
feedbacks = []

 

##Funcão que verifica se o caractere digitado é númerico

def numericValue(Userinput , message):
  while not Userinput.isnumeric():
    print(messages.numericError)
    Userinput = input(message)

  return Userinput

# ##Função que verifica se o númerio digitado é uma opção válida

def option_validation(numericInput , message):

   while not numericInput.isnumeric() or numericInput not in options :
       
       if not numericInput.isnumeric():
          print(messages.numericError)
       else:
           print(messages.optionError)

       numericInput = input(message)

   return numericInput


##Função que válida os logins 
def professional_login(username , password):
   
   if (username not in professional_usernames or password != "123"):
     print(messages.professional_login_error)
   else:
      print(messages.professional_login_success)
      taskOption = input(messages.professional_tasks)

      show_professional_tasks(taskOption)
      chosed_option_task(taskOption)
  
def patient_login(username , password):
   
   if (username not in patients_usernames or password != "432"):
     print(messages.professional_login_error)
   else:
      print(messages.professional_login_success)
      itemOption = input(messages.patients_items)
      show_user_items(itemOption)
      chosed_option_item(itemOption)

  
  
##Função que exibe as funções do lado profissional

def show_professional_tasks(task):
     
  numericValue(task, messages.professional_tasks)
  option_validation(task ,messages.professional_tasks)

 

 ##Função que valida qual taks foi escolhida


#Função que exibe as funcionalidades do lado do usuário 
def show_user_items(items):
     
  numericValue(items, messages.patients_items)
  option_validation(items ,messages.patients_items)


#Função que exibe o item escolhido
def chosed_option_item(itemOption):
   
   if itemOption == "1":
    print(messages.item01)
    my_prescp_medic()
     
   else: 
    print(messages.item02)
    patientMsg = input(messages.patientMsg)
    patient_feedback(patientMsg)


class prescption: 
  def __init__(self, patientId, medicineeName , medicineQnt , duration):
    self.patientId = patientId
    self.medice = medicineeName
    self.mediceQnt = medicineQnt
    self.duration = duration

  def __str__(self):
        return f"CPF DO PACIENTE: {self.patientId}, Nome do remédio: {self.medice}, Quantidade: {self.mediceQnt}, Duração do tratamento: {self.duration}"


def prescp_medic(patientId, medicineName , qntMedicine , duration):
    # Criando uma instância da classe prescption
    prescription_instance = prescption(patientId, medicineName, qntMedicine, duration)

    return(prescription_instance)



def my_prescp_medic():
   
   if len(prescriptions) == 0:
      print(messages.prescrip_error)
   else:
    print(prescriptions)

def patient_feedback(patientMsg):
    feedbacks.append(patientMsg)

    print("Feedback enviado com sucesso!")
    
  
def chosed_option_task(taskOption):
   
   if taskOption == "1":
    print(messages.task01)

    patientId = input(messages.patientId)
    medicineName = input(messages.medicineName)
    medicineQnt = input(messages.medicineQnt)
    medicineDuration = input(messages.medicineDuration)

    prescription_obj = prescp_medic(patientId, medicineName , medicineQnt, medicineDuration)
    print(prescription_obj)

    prescriptions.append(prescription_obj)

    taskOption = input(messages.professional_tasks)

    show_professional_tasks(taskOption)
    chosed_option_task(taskOption)
    
     
   else: 
    print(messages.task02)

    for i in prescriptions:
       print(i)
    

   
#Função que válida quais das opções foram digitdas

def chosed_option_login(loginOption):
   
   if loginOption == "1":
      print(messages.log_type_professional)
      professional_username = input(messages.user_name_professional)
      professional_psw = input(messages.password_professional)

      professional_login(professional_username , professional_psw)

      
      

   else: 
      print(messages.log_type_user)
      patient_username = input(messages.user_name_patient)
      patient_psw = input(messages.password_patient)
      patient_login(patient_username , patient_psw)

    

      




      

      
      
   
   









    
