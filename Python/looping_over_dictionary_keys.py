#!/usr/bin/env python3

def for_key_in_dict_keys():
    """Looping over the keys of a dictionary"""
    d = {"a": 1, "b": 2, "c": 3}
    for key in d:  # this is the same as `for key in d.keys()`
        pass

    for key in list(d):  # If we want to loop over keys to replace them, for example
        pass
