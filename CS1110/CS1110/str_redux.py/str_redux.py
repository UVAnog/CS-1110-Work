# Nph2tx
# Nolan Harris
'''First function checks to see if the part being looked for is in the whole code'''

def myfind(whole, part):

    if part in whole:
        for n in range(len(whole)):
            sub = whole[n:n+len(part)]

            if part in sub:
                return n
    # If it is not in the code, it returns -1 as it doesnt "exist"
    else:
        return -1


'''My split lists the mysplit and searches for the posistions of the parts '''


def mysplit(whole, part):

    split_word = []
    position_start = 0

    while part in whole[position_start::]:
        new_position = myfind(whole[position_start:], part)
        split_segment = whole[position_start: new_position+position_start]
        split_word.append(split_segment)
        if new_position == -1:
            position_start = new_position+len(part)+position_start

    split_word.append(whole[position_start:])
    return split_word
            


























