# Nolan Harris
# Nph2tx

def ellipsis(s):

    a = len(s) - 2
    x = s[:2]
    y = s[a:]
    return str(x) + "..." + str(y)

print(ellipsis("computer science"))

def eighteen(s):

    a = len(s) - 2
    b = len(s) - 1
    x = s[:1]
    y = s[b:]

    return str(x) + str(a) + str(y)

print(eighteen("computer scinece"))

def allit(s, t):

    x = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    string_1 = s.capitalize()
    string_2 = t.capitalize()

    if string_1[:1] == x:
        return "False"

    elif string_2[:1] == x:
        return "False"

    elif string_1[:1] == string_2[:1]:
        return "True"

    else:
        return "False"

print(allit("Hi", "Hello"))






