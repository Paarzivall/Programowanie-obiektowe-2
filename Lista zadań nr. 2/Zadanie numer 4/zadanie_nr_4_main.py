from zadanie_nr_4 import Rectangle, Cuboid
import linecache


file = open("dane.txt", "r")
"""


for i in range(count):
    lines = []
    lines.append(linecache.getline("dane.txt", i))
    print(lines)
"""
count = len(file.readlines())
for i in range(count):
    print(i)
    print(file.readline(i))


file.close()