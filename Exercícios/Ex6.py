#calculadora com while

while True:
    num1 = (input('digit the number one: ')) 
    num2 = (input('digit the number two:'))
    operator = input('choice the operator: (+, -, *, /): ')
    
    num_valid = None #flag for valid number
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        num_valid = True
    except:
        num_valid = None
        
    if num_valid is None: 
        print('Invalid number')
        continue
    
    operator_valid = '+-/*'
    
    if operator not in operator_valid: 
        print('Invalid operator')
        continue
    if len(operator) > 1:
        print('Digit only one operator')
        continue
    
    print('Realizing the operation... Look the result:')
    
    if operator == '+':
        print('The result is: ', num1 + num2)
    elif operator == '-':
        print('The result is: ', num1 - num2)
    elif operator== '*':
        print('The result is: ', num1 * num2)
    elif operator == '/':
        print('The result is:', num1 / num2)
    else:
        print('Invalid operator selected')
        continue

    exited = input('Run the exit? (s/n): ').lower().startswith('s') #retorna a string em minúsculo e verifica se começa com 's'
    if exited is True:
        break