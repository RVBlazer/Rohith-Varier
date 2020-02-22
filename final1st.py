
def check(n, list): #creating function check with 2 arguments
    if n in list:   #check if the number is in the list and if so,
        return True  #returning true
    return False     #returning False

x = input("Enter the number to be searched: ")   #input from user for the number to be searched
list = input("Enter the list with a comma after each number: ")    #the list to be entered on which the serach has to be performed.
print (check (x,list))   #2 arguments passed back to the function created and printing True or False depending on the input

