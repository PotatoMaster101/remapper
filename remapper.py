#!/usr/bin/env python3
###############################################################################
# remapper.py
# Remaps input characters to other randomised characters, effectively a 
# substitution cipher. 
#
# Author: PotatoMaster101
# Date:   20/04/2019
###############################################################################

import argparse
import string
import random
import sys
from collections import OrderedDict

def get_args():
    """
    Returns parsed arguments. 
    """
    p = argparse.ArgumentParser(description="Character remapper.")
    p.add_argument("input", type=str, 
            help="string to remap")
    p.add_argument("-v", "--verbose", action="store_true", dest="verbose", 
            help="produce verbose output")
    p.add_argument("-p", "--pool", type=str, dest="pool", default="", 
            help="pool of random characters that can be mapped")
    p.add_argument("-pA", "--pool-alph", action="store_true", dest="alph", 
            help="include all alphabetical characters")
    p.add_argument("-pN", "--pool-num", action="store_true", dest="num", 
            help="include all numerical characters")
    p.add_argument("-pL", "--pool-lower", action="store_true", dest="alphlow", 
            help="include all lower alphabetical characters")
    p.add_argument("-pU", "--pool-upper", action="store_true", dest="alphup", 
            help="include all upper alphabetical characters")
    p.add_argument("-pP", "--pool-punc", action="store_true", dest="punc", 
            help="include all punctuation characters")
    p.add_argument("-i", "--ignore", type=str, dest="ignore", default="", 
            help="pool of characters to ignore")
    p.add_argument("-iP", "--ignore-punc", action="store_true", dest="igp", 
            help="ignore all punctuations")
    p.add_argument("-iN", "--ignore-num", action="store_true", dest="ign", 
            help="ignore all numerical characters")
    p.add_argument("-e", "--error", type=str, dest="errchar", default="", 
            help="error character style")
    p.add_argument("-l", "--hints", type=str, nargs="+", dest="hints", 
            help="list of hints in the form of x=y", default=None)
    p.add_argument("-o", "--out-file", type=str, dest="outf", default="", 
            help="output file to write to")
    p.add_argument("-f", "--from-file", action="store_true", dest="fromf", 
            help="indicates that the input is a file name")
    return p


def get_mapped(inp, pool, ignore, errchar, hints):
    """
    Returns the mapped string and the map used. 
    """
    mapper = {}
    output = ""
    for h in hints:                 # map hints
        x, y = parse_hint(h)
        pool = pool.translate(str.maketrans("", "", x + y))
        for (l, h) in zip(x, y):
            mapper[l] = h
            mapper[h] = l
    for ch in ignore:               # map ignored chars
        mapper[ch] = ch

    for ch in inp:
        if ch in mapper:    # char already mapped
            output += mapper[ch]
            continue
        if not pool:        # no more char in pool
            mapper[ch] = errchar
        else:               # get random char from pool
            mapper[ch] = random.choice(pool)
            pool = pool.replace(mapper[ch], "")
        output += mapper[ch]
    return output, mapper


def get_pool(argp):
    """
    Returns a pool of characters used for randomisation. 
    """
    ret = argp.pool
    if argp.alph:
        ret += string.ascii_letters
    if argp.num:
        ret += string.digits
    if argp.alphlow:
        ret += string.ascii_lowercase
    if argp.alphup:
        ret += string.ascii_uppercase
    if argp.punc:
        ret += string.punctuation
    if not ret:
        ret += string.ascii_letters + string.digits + string.punctuation
    return "".join(set(ret))


def get_ignore(argp):
    """
    Returns a pool of characters which will be ignored. 
    """
    ret = argp.ignore
    if argp.igp:
        ret += string.punctuation + " \n\r"
    if argp.ign:
        ret += string.digits
    return "".join(set(ret))


def get_input(argp):
    """
    Returns the user input. 
    """
    if not argp.fromf:
        return argp.input
    with open(argp.input) as f:
        return f.read()


def parse_hint(hint):
    """
    Parses the given hint in the form of x=y, returns x and y. 
    """
    split = hint.split("=")
    if (len(split) != 2) or (not split[0]):     # test split[0] or split[1]
        print("[-] Failed to parse %s, not using." %hint)
        return "", ""
    split[0] = "".join(OrderedDict.fromkeys(split[0]))
    split[1] = "".join(OrderedDict.fromkeys(split[1]))
    if len(split[0]) != len(split[1]):
        print("[-] Counts of hint %s are not equal, not using." %hint)
        return "", ""
    return split[0], split[1]


if __name__ == "__main__":
    """
    Entry point. 
    """
    argp = get_args().parse_args()
    usrinp = get_input(argp)
    pool = get_pool(argp)
    ignore = get_ignore(argp)
    outf = sys.stdout if not argp.outf else open(argp.outf, "w+")
    errchar = "<ERROR>" if not argp.errchar else argp.errchar
    hints = [] if not argp.hints else argp.hints
    pool = pool.translate(str.maketrans("", "", ignore))

    output, mapper = get_mapped(usrinp, pool, ignore, errchar, hints)
    if argp.verbose:
        print("[+] Map:      %s" %mapper)
        print("[+] Original: %s" %usrinp)
        print("[+] Unique:   %s" %len("".join(set(usrinp))))
        print("[+] Pool:     %s" %pool)
        print("[+] Ignored:  %s" %ignore)
        print("[+] Hints:    %s" %hints)
        print("[+] Error:    %s" %errchar)
    print(output, file=outf)
    if argp.outf:
        outf.close()

