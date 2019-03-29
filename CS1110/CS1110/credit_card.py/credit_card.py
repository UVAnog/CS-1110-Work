# Nolan Harris
# Nph2tx


def check(s):
    ''' get the sum of the numbers, make sure it is divisible by 2'''
    n = 0
    while s:
        n += s % 10
        s //= 10
    if n % 2 == 0:
        return n
    '''If it is divisible by 2, '''





