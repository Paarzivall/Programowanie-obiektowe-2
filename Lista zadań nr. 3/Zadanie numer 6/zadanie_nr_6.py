"""def flatten(data):
    for x in data:
        if isinstance(x, list):
            yield from flatten(list(x))
        elif isinstance(x, tuple):
            yield from flatten(list(x))
        else:
            yield x


if __name__ == '__main__':
    all = []
    for x in flatten(([1, 'kot'], 3, (4, 5, [7, 8, 9]))):
        all.append(x)
    print(all)"""

import collections.abc

def flatten(data):
    for x in data:
        if isinstance(x, collections.abc.Iterable) and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


if __name__ == '__main__':
    all = []
    for x in flatten(([1, 'kot'], 3, (4, 5, [7, 8, 9, {2, 3, 4, (9, 8)}]))):
        all.append(x)
    print(all)