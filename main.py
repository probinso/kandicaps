

fd = open("bibleverse.txt")
indata = fd.read()
fd.close()

def altchars(data):
    f = lambda index, char : (str.upper, str.lower)[index%2](char)
    retval = ""
    for index, char in enumerate(data):
        retval += f(index, char)
    return retval

def isVowel(char):
    lowerchar = str.lower(char)
    vowels = ['a','e','i','o','u','y']
    return lowerchar in vowels
    

altdata = altchars(indata)
altwords = altdata.split()
for w in altwords:
    for c in w:
        print isVowel(c)
