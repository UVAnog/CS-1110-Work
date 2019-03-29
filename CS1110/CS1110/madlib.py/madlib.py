# Nolan Harris
# nph2tx
# kbs5fp

'''The following prompts the user for 4 nouns, 3 verbs, 2 adjectives, and 1 occupation'''

print ("Welcome to your madlib! Please fill out the following fields. ")

#Nouns

n1 = str(input("Noun 1: "))

n2 = str(input("Noun 2: "))

n3 = str(input("Noun 3: "))

n4 = str(input("Noun 4: "))

#Verbs

v1 = str(input("Verb 1: "))

v2 = str(input("Verb 2: "))

v3 = str(input("Verb 3: "))

#Adjectives

a1 = str(input("Adjective 1: "))

a2 = str(input("Adjective 2: "))

a3 = str(input("Adjective 3: "))

#Occupation

o1 = str(input("Profession: "))

def func1():
    '''Prints madlib'''
    print ("Today a " + o1 + " named " + n1 + " came to our school to talk to us about her job. "
           "She said the most important skill you need to know to do her job is to be able to "
           + v1 + " around (a) " + a1 + " dirty " + n2 + ". She said it was easy for her to learn her job because she loved to "
           +  v2 + " when she was my age, and that helps a lot! If you're considering her profession, I hope you can be near "
           +  a2 + " " + n3 + " That's very important! If you get too distracted in that situation you won't be able to " +
           v3 + " next to (a) " + n4 + "!")

func1()


