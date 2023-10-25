import random

def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra , papel o tijera =>')
  user_option = user_option.lower()#reconoce todas las letras como minuscula
  computer_option = random.choice(options)#choice escoge algo casual de un tuple
 
  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None, None
    
  print('user option =>', user_option)
  print('computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print ('Empate!')
    
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print ('piedra gana a tijera')
      print ('user gano!')
      user_wins += 1
      
    else:
      print('papel gana a piedra')
      print ('computer gano!')
      computer_wins += 1
      
  elif user_option == 'papel':
    if computer_option == 'piedra':
     print ('papel gana a piedra')
     print('user gano')
     user_wins += 1
      
    else:
      print ('tijeras gana a papel')
      print('computer gano!')
      computer_wins += 1
      
  elif user_option == 'tijera':
    if computer_option =='papel':
      print ('tijera gana a papel')
      print ('user gano!')
      user_wins += 1
      
    else:
      print ('piedra gana a tijera')
      print('computer gano')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
    
  while True:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    
    rounds += 1
  
    user_option, computer_option = choose_option()
    
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
    if computer_wins == 2:
      print('EL GANADOR ES COMPUTER')
      break
      
    if user_wins == 2:
      print ('EL GANADOR ES USER')
      break
        
run_game()