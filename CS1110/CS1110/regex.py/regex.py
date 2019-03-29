# Nolan Harris
# Nph2tx

import re

nospace = re.compile(r"[^\s]+")

quotation = re.compile(r"\"[^\s][^\"]+[^\s]\"")

twonum = re.compile(r'(-?[0-9]+([\.]+[0-9]+)?)(,|,\s|\s)(-?[0-9]+([\.]+[0-9]+)?)')

