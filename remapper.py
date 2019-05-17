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

def get_args():
    """
    Returns parsed arguments. 
    """
    p = argparse.ArgumentParser(description="Character remapper.")
    p.add_argument("input", type=str, 
            help="string to remap")
    p.add_argument("-v", "--verbose", action="store_true", 
            help="produce verbose output")
    p.add_argument("-p", "--pool", type=str, dest="pool", default=None, 
            help="pool of random characters that can be mapped")
    p.add_argument("-i", "--ignore", type=str, dest="ignore", default=None, 
            help="pool of characters to ignore")
    p.add_argument("-e", "--error", type=str, dest="errchar", default=None, 
            help="error character style")
    p.add_argument("-l", "--list", type=str, nargs="+", dest="hints", 
            help="list of hints in the form of x=y", default=None)
    return p


def get_mapped(inp, pool, ignore, errchar, hints):
    """
    Returns the mapped string and the map used. 
    """
    mapper = {}
    output = ""
    for h in hints:                 # map hints
        x, y = parse_hint(h)
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


def parse_hint(hint):
    """
    Parses the given hint in the form of x=y, returns x and y. 
    """
    split = hint.split("=")
    if len(split) != 2:
        return [], []
    if len(split[0]) != len(split[1]):
        return [], []
    return split[0], split[1]


if __name__ == "__main__":
    """
    Entry point. 
    """
    argp = get_args().parse_args()
    errchar = "<ERROR>"
    if argp.errchar:
        errchar = argp.errchar
    pool = string.ascii_letters + string.digits + string.punctuation
    if argp.pool:
        pool = argp.pool
    ignore = ""
    if argp.ignore:
        ignore = argp.ignore
        pool = pool.translate(str.maketrans("", "", ignore))
    hints = []
    if argp.hints:
        hints = argp.hints
    inpstr = argp.input

    output, mapper = get_mapped(argp.input, pool, ignore, errchar, hints)
    if argp.verbose:
        print("[+] Map:      %s" %mapper)
        print("[+] Original: %s" %inpstr)
        print("[+] Ignored:  %s" %ignore)
        print("[+] Hints:    %s" %hints)
        print("[+] Output:   ", end="")
    print(output)
