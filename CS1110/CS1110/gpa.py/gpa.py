# Nolan Harris
# Nph2tx

Gpa = 0
total_credits = 0

def add_course(grade, credits=3):
    global total_credits
    global Gpa
    Gpa = ((Gpa*total_credits) + (grade*credits))/(total_credits+credits)
    total_credits = total_credits + credits

def credit_total():
        return total_credits

def gpa():
     return Gpa