import time


def time_code_execution():
    """
    This is a common way to time the execution of a code block.
    """
    start_time = time.time()  # time.time() is really to tell the current time
    # Code block to be timed
    # ...
    end_time = time.time()
    return end_time - start_time

    # Here is a better option to time the execution of a code block:
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    return end - start
