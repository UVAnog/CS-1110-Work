#Nph2tx

def binop(s):

    '''If statements finding the operator'''

    if s.find("+")!= -1:
        t = s.find("+")
        f = int(s[0:t])
        last = int(s[t+1:])
        return f + last

    if s.find("-")!= -1:
        t = s.find("-")
        f = int(s[0:t])
        last = int(s[t+1:])
        return f - last

    if s.find("*") != -1:
        t = s.find("*")
        f = int(s[0:t])
        last = int(s[t+1:])
        return f * last

    if s.find("/") != -1:
        t = s.find("/")
        f = int(s[0:t])
        last = int(s[t+1:])
        return f / last























