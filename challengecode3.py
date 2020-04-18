from random import randint

input1= randint(10,25)
input2= randint(200,400)

print("The car can travel " + str(input2 // input1) + " miles per gallon.")
print("The car's fuel tank can hold " + str(input1) + " gallons.")
print("The car can travel " + str(input2) + " miles on a full tank.")

