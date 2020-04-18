celsius = int(raw_input("Please enter integer value of celsius "))
def fahrenheit(celsius):
	F = 1.8*celsius + 32
	final=round(F,1)
	print("The Fahrenheit equivalent of " +str(celsius)+" degrees Celsius is " +str(final)+ ".")

fahrenheit(celsius)
