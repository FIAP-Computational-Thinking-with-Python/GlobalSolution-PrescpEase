import Myfunctions
import messages



print(messages.decoration_line)
print(messages.welcome_message)
print(messages.decoration_line)
print(messages.login_message)
print(messages.decoration_line)

userInput = input(messages.log_type_message)

##Ativa a function numericValue()

numericInput = Myfunctions.numericValue(userInput , messages.log_type_message)

loginOption =  Myfunctions.option_validation(numericInput , messages.log_type_message)

Myfunctions.chosed_option_login(loginOption)







