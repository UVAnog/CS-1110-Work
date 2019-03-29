# Nolan Harris
# Nph2tx

import urllib.request
import re


def name_to_url(name):  # This function returns a properly formatted name from the url
    """

    :param name: name input for person
    :return: name hyphenated
    """
    if type(name) == int:
        return name
    elif ', ' in name:
        index1 = name.find(', ')
        last = name[:index1]
        first = name[index1 + 2:]
        first = first.lower()
        last = last.lower()
        formatted = first + '-' + last
        return formatted
    elif ' ' in name:
        index1 = name.find(' ')
        first = name[:index1]
        last = name[index1 + 1:]
        first = first.lower()
        last = last.lower()
        formatted = first + '-' + last
        while ' ' in formatted:
            index2 = formatted.find(' ')
            combined = formatted[:index2]
            second = formatted[index2 + 1:]
            formatted = combined + '-' + second
        return formatted
    else:
        return name


def get_job_title(person):  # This function gets the title of the argument person from the URL
    """

    :param person: name input of person
    :return: job title for person
    """
    base_url = 'http://cs1110.cs.virginia.edu/files/uva2016/'
    url = base_url + person
    try:
        stream = urllib.request.urlopen(url)
        title = re.compile(r'<meta property="og:description" content="Job title: (.+)<br /> 2016 total gross pay:')
        for line in stream:
            line = line.decode('utf-8')
            if title.search(line) != None:
                for m in title.finditer(line):
                    rank = m.group(1)
                    if '&amp;' in rank:
                        index1= rank.find('&amp;')
                        rank = rank[:index1]+'&'+rank[index1+5:]
                    if '&lt;' in rank:
                        index1 = rank.find('&lt;')
                        rank = rank[:index1] + '<' + rank[index1 + 4:]
                    if '&gt;' in rank:
                        index1 = rank.find('&gt;')
                        rank = rank[:index1] + '>' + rank[index1 + 4:]

                    return rank

    except urllib.error.HTTPError:
        return None


def get_rank(person):  # This function finds the 'rank' of the person as an integer
    """

    :param person: name input
    :return: salary rank
    """
    base_url = 'http://cs1110.cs.virginia.edu/files/uva2016/'
    url = base_url + person
    try:
        stream = urllib.request.urlopen(url)
        rank = re.compile(r'<tr><td>University of Virginia rank</td><td>(.+) of 7,927</td></tr>')
        number = 0
        for line in stream:
            line = line.decode('utf-8')
            if rank.search(line)!= None:
                for m in rank.finditer(line):
                    number = m.group(1)
                    if ',' in number:
                        index_ = number.find(',')
                        number = number[:index_] + number[index_ + 1:]
        return int(number)

    except urllib.error.HTTPError:
        return 0


def get_salary(person):  # The get_salary function returns the pay of the person found
    """

    :param person: name input for person
    :return: salary for person
    """
    url_normal = 'http://cs1110.cs.virginia.edu/files/uva2016/'
    url = url_normal + person
    try:
        stream = urllib.request.urlopen(url)
        pay = re.compile(r'<div style=\"margin:0; float:left; background:#337ab7; height:100%; width:<%= getPct\(paytype\.amount, (.+)\) %>%;\"></div>')
        for line in stream:
            line = line.decode('utf-8')
            if pay.search(line) != None:
                for m in pay.finditer(line):
                    pay = m.group(1)
                    if ',' in pay:
                        index_ = pay.find(',')
                        pay = pay[:index_]+pay[index_+1:]
                    return float(pay)
    except urllib.error.HTTPError:
        return 0


def report(name):  # The report calls on the functions to compile them into a result
    """

    :param name: the person who is being searched for
    :return: returns the job title, salary and rank of the input person
    """
    name = name_to_url(name)
    job = get_job_title(name)
    money = get_salary(name)
    rank = get_rank(name)
    return job, money, rank

