while True:

    print('Input two arbitrary numbers or press X to exit')

    a = (input('Enter your first number')).strip()
    
    if a == 'X' or a == 'x':
        print('Goodbye!')
        break
    
    
    b = (input('Enter your second number')).strip()
    
    if b == 'X' or b == 'x':
        print('Goodbye!')
        break

    
    
    result = int(a)  + int(b)
    print(f"The sum of the two numbers you entered is {result}") 















