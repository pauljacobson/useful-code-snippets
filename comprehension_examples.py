#!/usr/bin/env python3

def comprehension_examples():
    dict_comp = {i: i * i for i in range(10)}  # Dictionary comprehension
    list_comp = [x*x for x in range(10)]  # List comprehension 
    set_comp = {i%3 for i in range(10)}  # Set comprehension 
    gen_comp = (2*x+5 for x in range(10))  # Generic comprehension ?
    

if __name__ == "__main__":
    comprehension_examples()
