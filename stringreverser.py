entered_string = raw_input("Please enter a string: ")

reversed = ""

for item in range(len(entered_string) -1, -1, -1):
    reversed += entered_string[item]

print(reversed)
