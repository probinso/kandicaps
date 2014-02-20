

fd = open("bibleverse.txt")
indata = fd.read()
fd.close()

def altchars(data):
    f = lambda index, char : (str.upper, str.lower)[index%2](char)
    retval = ""
    for index, char in enumerate(data):
        retval += f(index, char)
    return retval

indata = altchars(indata)

def preservewhite(data):
    for index, ch in enumerate(data):
        if not str.isspace(ch): break
    return data[:index], data[index:]

def getword(data):
    for index, ch in enumerate(data):
        if str.isspace(ch): break
    return data[:index], data[index:]

def rules(data):
    acc, rest = preservewhite(data)
    word, rest = getword(rest)

    k = 0
    for index, ch in enumerate(word):
        if isVowel(ch):
            acc += str.lower(ch)
            k = index
        elif str.lower(ch) is 'l':
            acc += 'L'
        else:
            pass
