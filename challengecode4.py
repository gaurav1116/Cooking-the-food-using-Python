score = int(raw_input("Please enter your score: "))

if(score>=90):
    print("The grade is A")
else:    
    if(score>=80):
        print("The grade is B")
    else:
        if(score>=70):
            print("The grade is C")
        else:	    
            if(score>=60):
                print("The grade is D")
            else:
                print("The grade is F")
