

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
