integer= int(input("Please enter and integer greater than 0"))
entered_integer=integer
counter=0

while integer>0:

    counter+=integer
    
    integer-=1

print("The entered integer is " +str(entered_integer)+ "and the required sum is " +str(counter)+".")  
