def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100")
        
    elif score >= 90:
        print("Grade is A")
    elif score >= 80:
        print("Grade is B")
    elif score >= 70:
        print("Grade is C")
    elif score >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
        
while True:
    score = int(input("Ano ang Grade mo?"))
    assign_grade(score)
        
        