import urllib.request

start = True

while start:
    link = 'http://cs1110.cs.virginia.edu/files/words.txt'
    enter = input('Type some words. Enter a blank line to stop: ')
    checker = []
    word = []

    if enter == '':
        start = False
        exit()
    stream = urllib.request.urlopen(link)
    for line in stream:
        data = line.decode("UTF-8").strip()
        checker.append(data)
    item = enter.split()
    wordlist = []
    for x in item:
        y = x.strip(".?!,()\"'")
        wordlist.append(y)

    for part in wordlist:
        if part.lower() not in checker:
            print("MISSPELLED: " + part)













