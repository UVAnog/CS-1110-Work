#Nolan Harris
#Nph2tx

'''Shift functions. Takes text and encrypts it by adding the key to the index'''
def encrypt_shift(text,key):
    letter = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    cypher_text = ''
    for i in text:
        index = alphabet.find(i)
        new_letter = alphabet[index + key]
        new += new_letter

    return new
print(encrypt_shift('hello', 3))
'''decrypts the text that was encrypted, or encrypted text the user inputs'''
def decrypt_shift(text, key):
    letter = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    cypher_text = ''
    for i in text:
        index = alphabet.find(i)
        new_letter = alphabet[index - key]
        new += new_letter
    return new
print(decrypt_shift('khoor', 3))

#


#print(encrypt_vignere('hello', 'hi'))

a_list = [5, 10, 15, "20"]
print(a_list.pop(3)[1] == False)

def what_I_do(a_list):
    new_list = []
    for i in a_list:
        new_list.append(abs(i))
    print(new_list.sort())

    what_I_do([3,4,-5,6,7-8,-9])
    