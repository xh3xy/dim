import math

KiB = math.pow(1024, 1)
MiB = math.pow(1024, 2)
GiB = math.pow(1024, 3)
TiB = math.pow(1024, 4)
PiB = math.pow(1024, 5)

HUMAN_READABLE_SIZE = {KiB, MiB, GiB, TiB, PiB}

def as_human_readable(n_bytes, precision=1):
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']

    magnitude = 0
    remainder = n_bytes

    while remainder >= 1024:
        if magnitude + 1 < len(units):
            magnitude += 1
            remainder /= 1024
        else:
            break

    if magnitude == 0:
        remainder = round(remainder)
    else:
        remainder = round(remainder, precision)

    return f'{remainder} {units[magnitude]}'
