from zadanie_nr_4 import Rectangle, Cuboid


file = open("dane.txt", 'r').read()
lines = file.split("\n")
print(lines)

for line in lines:
    list(set(line))
    if line[0] == '1':
        print(line)
        lin = line.split(" ")
        for x in lin:
            x = float(x)
        print(type(line))





