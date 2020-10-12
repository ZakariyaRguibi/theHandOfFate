import json
import re
import pprint


def pretty(d, indent=0):
    """return a pretty string of the dict data"""
    text = ""
    for key, value in d.items():
        if key in ["aon", "pfs", "src", "source"]:
            continue
        text = text + ("\t" * indent) + "**" + str(key) + "**:"
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            text = text + ("\t" * (indent + 1)) + str(value) + "\n"
    return text


def indexing():
    """creates a list of lowercase names from pf2 json"""
    with open("data/pf2.json") as json_file:
        data = json.load(json_file)
        names = []
        for elm in data:
            names.append(elm["name"].lower())
        with open("data/index.json", "w") as outfile:
            json.dump(names, outfile)


def lookupIndex(L, target):
    """binary search algorithm for pf2 json
    L: sorted List
    target: search subject
    """
    target = target.lower()
    start = int(0)
    end = int(len(L) - 1)
    while start <= end:
        middle = int((start + end) / 2)
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle
    return None


def lookupWc(L, target):
    """lookup similar shit"""
    i = 0
    wild_results = ""
    for elm in L:
        i = i + 1
        if re.search(target, elm):
            wild_results = wild_results + elm + "\n"
    return wild_results


def lookup_str(target):
    """lookup a string in the pf jsons"""
    f_indexs = open(
        "data/index.json",
    )
    f_pf2e = open(
        "data/pf2.json",
    )
    indexes = json.load(f_indexs)
    pf2e = json.load(f_pf2e)
    index = lookupIndex(indexes, target)
    if index is None:
        return lookupWc(indexes, target)
    else:
        return pf2e[index]