def index_counter_variable():
    """Creating an index counter variable"""
    l = [1, 2, 3, 4, 5]

    # This is a common construction in Python
    # It isn't a good practice to use it, though
    index = 0
    for x in l:
        print(index, x)
        index += 1

    # This is a better way to do it
    for i, x in enumerate(l):  # If we're starting at index = 0, use enumerate() instead
        pass
