#!/usr/bin/env python

import re
import sys

"""
aRe tHeRe RuLeZ yOu FoLLoW wHeN TyPiNg LiKe a GooBeR? cLeaRLy, LiKe
HeLLo?!?!?! oF CouRse tHeRe aRe!!! tHe RuLeZ oF CaNdY CaPs:
"""

def isvowel(char):
    from random import random
    char = char.lower()

    vowels = 'a', 'e', 'i', 'o', 'u'
    if char in vowels:
        return True
    if char == 'y':
        return random() < 0.5
    return False


def isconsonant(char):
    from strings import ascii_lowercase
    char = char.lower()
    return (char in ascii_lowercase) and not isvowel(char)


def next_cond(arry, cond):
    for i, elem in enumerate(arry):
        if cond(elem): return i
    return None


def split_tup(text):

    space = str.isspace
    notspace = lambda x: not space(x)

    start = 0
    while True:
        end = next_cond(text[start:], space)
        if end is None: break
        yield text[start:start+end]

        wsp = next_cond(text[start+end:], notspace)
        if wsp is None: break
        yield text[start+end:start+end+wsp]

        start = start + end + wsp


def one(word):
    """
    1. nO BiG e'S, nO LiTTLe L's!
    """
    return word.replace('E', 'e').replace('l', 'L')


def two(word):
    """
    2. iF tHe SeCoND LeTTeR iS a VoWeL, uPPeRCaSe tHe FiRsT LeTTeR!
    """
    if next_cond(word, isvowel)==1:
        word = word[0].upper() + word[1:]
    return word


def three(word):
    """
    3. iF tHe FiRsT LeTTeR iS a VoWeL, LoWeRCaSe tHe FiRsT LeTTeR!
    """
    if next_cond(word, isvowel)==0:
        word = word[0].lower() + word[1:]
    return word


def four(word):
    """
    4. iF tHe FiRsT aND SeCoNd aRen't VoWeLs, BuT tHe tHiRd iS, LoWeRCaSe
    tHe FiRsT sO tHe tHiRd WiLL Be LoWeRcaSeD!
    """
    if next_cond(word, isvowel)==2:
        word = \
            word[0].lower() + word[1].upper() + word[2].upper() + word[3:]
    return word


def five(word):
    """
    5. iF tWo CoNSeNaNtS aRe SuRRoUnDeD bY VoWeLs, tHeN tHe tWo CoNseNaNtS
    aRe uSuaLLy uPPeRCaSe (LiKe iN uPPeRCaSe tHe P's) sO tHaT tHe VoWeLs
    WiLL BoTh eNd uP LoWeRCaSeD!
    """
    _ = ''.join(map(str, map(int, map(isvowel, word))))
    up_mid = [m.start() for m in re.finditer('1001', _)]
    lo_mid = [m.start() for m in re.finditer('0110', _)]
    li = list(word)
    for start in up_mid:
        li[start] = li[start].lower()
        li[start+1] = li[start+1].upper()
        li[start+2] = li[start+2].upper()
        li[start+3] = li[start+3].lower()

    for start in lo_mid:
        li[start] = li[start].upper()
        li[start+1] = li[start+1].lower()
        li[start+2] = li[start+2].lower()
        li[start+3] = li[start+3].upper()

    return ''.join(li)

def main():
    with open("bibleverse.txt") as fd:
        indata = fd.read()

    g = split_tup(indata)

    def rules(word, *rules):
        for rule in rules:
            word = rule(word)
        return word

    for word in g:
        word = rules(word, one, two, three, four, five)
        sys.stdout.write(word)
        sys.stdout.write(next(g, ''))


if __name__ == '__main__':
    main()
