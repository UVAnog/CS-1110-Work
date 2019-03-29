# Nolan Harris
# Nph2tx


import urllib.request
import re

# This opens the url and creates a blank list to add the email matches to
stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')
hits = []
for line in stream:
    decoded = line.decode('UTF-8').strip()
    decoded = decoded.replace('DOT', '.')
    decoded = decoded.replace('dot', '.')
    decoded = decoded.replace('AT', '@')
    decoded = decoded.replace('at', '@')
    matches = re.compile(r'[\w.-]+@[\w.-]+')
    x = matches.findall(decoded)
    if x != []:
        hits.append(x)

print(hits)





