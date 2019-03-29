# Nph2tx
# Nolan Harris

"""Creates a global variable grade book to store the values and assignments"""
gradebook = {}

def assignment(kind, grade, weight = None):
    ''' Adds the weight if assumed as 1'''
    if not weight:
        weight = 1
    global gradebook

    '''Checks for the kind in the grade book'''
    if kind in gradebook:
        gradebook[kind][0] += grade * weight
        gradebook[kind][1] += weight
    else:
        gradebook[kind] = [grade * weight, weight]

    '''Looks to find the average for all of the assingments and return it'''


def total(proportions):
    average = {}
    for key, value in gradebook.items():
        if key in average:
            average[key] += value[0] / value[1]
        else:
            average[key] = value[0] / value[1]
    grade = 0
    for key in average.keys():
        if key in proportions:
            grade += average[key] * proportions[key]
    return grade




