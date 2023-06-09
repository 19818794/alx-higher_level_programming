#!/usr/bin/python3
"""
101-stats module contains a script that reads stdin line by line
and computes metrics.
"""
import sys


def print_status(size, codes):
    """
    prints statistics.
    args:
    size (int): the total size of the read files.
    codes (dict): a count of all status codes.
    """
    print("File size: {}".format(size))
    for i in sorted(codes):
        if codes[i] > 0:
            print("{}: {}".format(i, codes[i]))


if __name__ == "__main__":
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    size = 0
    counter = 0
    try:
        for line in sys.stdin:
            if counter == 10:
                print_status(size, codes)
                counter = 1
            else:
                counter += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (ValueError, IndexError):
                pass
            try:
                code = int(line[-2])
                if code in codes:
                    if codes.get(code, -1) == -1:
                        codes[code] = 1
                    else:
                        codes[code] += 1
            except (ValueError, IndexError):
                pass
        print_status(size, codes)
    except KeyboardInterrupt:
        print_status(size, codes)
        raise
