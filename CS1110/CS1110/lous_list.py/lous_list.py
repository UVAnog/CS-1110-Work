# Nolan Harris
# Nph2tx
import urllib.request


def instructors(department):
    names = []
    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + department
    data = urllib.request.urlopen(url)
    for line in data:
        name = line.decode("UTF-8").strip().split("|")[4]
        if '+' in name:
            name = name[0:len(name)-2]
        if name not in names:
            names.append(name)
    names.sort()
    return names


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):

    classes = []
    enrollment = []
    for i in range(0, 6):
        enrollment.append(dept_name)
        if has_seats_available:
            enrollment.append(has_seats_available)
        if level:
            enrollment.append(level)
        if not_before:
            enrollment.append(not_before)
        if not_after:
            enrollment.append(not_after)
        if len(enrollment) > 5:
            enrollment.remove(enrollment[0])
            classes.append((list(enrollment), enrollment[0]))

    return classes





