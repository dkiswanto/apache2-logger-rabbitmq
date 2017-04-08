import time

# Implemented from here,
# http://www.dabeaz.com/generators/
# Generator Tricks for Systems Programmers


def log_generator(file):
    # make the pointer go the end of file
    file.seek(0, 2)

    while True:
        # read on each line
        line = file.readline()

        # check if line (log message) not empty
        if not line:

            # delay the process, and DON'T Generate the empty line
            time.sleep(0.1)
            continue

        # generate the log string to generators
        # check out about python yield keyword and generator here
        # https://docs.python.org/2.4/ref/yield.html
        yield line

