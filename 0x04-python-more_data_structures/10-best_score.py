#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary.values()) > 0:
        for key in a_dictionary.keys():
            if a_dictionary[key] == max(a_dictionary.values()):
                return key
    return None
