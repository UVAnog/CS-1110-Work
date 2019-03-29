#Nolan Harris
#Nph2tx

'''This asks for a word'''

string = input('Enter a word!: ').lower()
string1 = ("_".join(string))
done = string1.find('_')
print(string1)
'''This asks them for a letter'''

letter = input('Guess a letter!: ').lower()
while string1.find('_') != -1:
    ''' The original line of text replacing the letter'''
    if letter in string1:
        letter1 = letter*2
        string1 = string1.replace(letter + '_', letter1)
        print(string1)

    elif letter not in string1:
        print('Guess again!' + ' ' + string1)
    elif letter in string1:
        print("done!")


