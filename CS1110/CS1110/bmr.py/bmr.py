# Nolan Harris
# Nph2tx

def st_jeor(mass, height, age, sex):

    if sex == "male" or sex == "Male":
        x = 5
    elif sex == "female" or sex == "Female":
        x = -161

    p = 10 * mass + 6.25 * height - 5.0 * age + x
    return p



