def pyth(n):  #creating the function with one argument

    if n==0:      #if the number given by user is 0
      return 0  
    x=1
    sum=1
    if n==1:     #if the number given by user is 1
        return 1
    
    for i in range(1,n):   #for loop for in the range of 1 to n
        sum=sum+(1/(x+2))   
        x=x+2
    return sum      # print sum in loop multiple times
    
  
n=int(input('Enter the value:::'))        #asking the user to enter the number till which the sum needs to be done


sum1=pyth(n)      #passing the argument back to the function while calling it  
print(sum1)
