"""def fib():
    a, b = 0, 1
    while True:
        yield a
        tmp = a
        a = b
        b += tmp
"""
def fib(n):
    a = 0
    b = 1
    c = 1
    yield a
    while c < n:
        a, b = b, a + b
        if a % 2 == 0:
            yield a
            c += 1
    return a


for i, f in enumerate(fib(100000), 1):
    print("{:3d}.  {:d}".format(i, f))
"""
for i in range(ile):
    print(f"{i + 1} wyraz ciągu:\t{next(fib(ile))}")
"""