number = input("Enter a number to get the factorial ")

def fact(number):
    
    returned =1
   
    for number in range(number,1,-1):
    
        returned *= number

    return returned

print("The factorial of " +str(number)+ " is " +str(fact(number)) + " .")

