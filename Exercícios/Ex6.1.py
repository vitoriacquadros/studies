# calculator in python using functions 

print('Welcome to the calculator in python!')
print('This calculator is very simple, but it´s very useful for you!')
print('Let´s start?')

def calculator(num1, num2, operator):
    if operator == '+':
        return (num1 + num2)
    elif operator == '-':
        return num1 - num2
    elif operator== '*':
        return (num1 * num2)
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid operator selected'

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
    
    print(calculator(num1, num2, operator))

    exited = input('Run the exit? (s/n): ').lower().startswith('s') 
    if exited is True:
        print('Bye!')
    else:
        print('Ok, let´s continue!')

