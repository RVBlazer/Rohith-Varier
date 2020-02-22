def digits(n):   #creating digits function with one argument
       
    print('\n \nThe list you need is as follows:- \n \n') 
    random=list(n)   #using the list predefined/built in function to extract characters/elements from the string
    print(random)    #printing the digits seperately

n=input('Enter the value: \n \n')  #input by the user
print('\n \nThe number you have provided is as follows: \n \n'+ n)     
digits(n)  #passing the argument back to the function while calling it
