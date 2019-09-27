answer = "Watson"
print ("Here is a guessing  game. You get three tries. ")
print ("What is the name of the computer that played on Jeopardy?")
response = input()
if response == answer:
    print("That is right!") 
else:    
    print("Sorry. Guess again: ")   
    response = input()
if response == answer:
    print("That is right!")
else:
    print("Sorry. One more guess:")
    response = input()
if response == answer:
    print ("That is right!")
else:
    print("Sorry. Np more guesses. The answer is " + ".")  
         