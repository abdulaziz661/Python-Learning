op1 = 0.0
op2 = 0.0
op = ''
while op1 != 'q':
    print("Enter first number (q to quit): ")
    op1 = input()
    if op1 == 'q':
       break;
       op1 = float(op1)
       print("Enter second number: ")
       op2 = float(input())
       print("Enterr an operation +,-,*,/): ")
       op = input()
       if op == '+':
           print(op1 + op2)
       elif op == '-':
           print(op1-op2)  
       elif op == '*':
           print(op1 * op2 )       
       elif op == '/':
           print(op1 / op2) 
       else: 
           print("did not recognise operator.")       