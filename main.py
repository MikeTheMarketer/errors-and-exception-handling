def error_example():
  try:
    user_input = int(input("Please enter your number for division: "))
    
    while user_input > 0:
      number_divide = user_input / 0
      
  except NameError:
    print('Wrong name type')
    
  except ValueError:
    print('Wrong value error')
    
  except ZeroDivisionError:
    print('You cannot divide by 0!')
    
error_example()
    