from tkinter import *
from  Triangle import Triangle
from IsoscelesTriangle import IsoscelesTriangle
from EquilateralTriangle import EquilateralTriangle
from ConvexQuadrilateral import ConvexQuadrilateral
from RegularPentagon import RegularPentagon
from RegularHexagon import RegularHexagon
from RegularOctagon import RegularOctagon


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}')
canvas = Canvas(root, bg="white", width=screen_width/2, height=screen_height/2)


def triangle_function():
    triangle = Triangle('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def triangle1_function():
    triangle = IsoscelesTriangle('red', 'blue')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def triangle2_function():
    triangle = EquilateralTriangle('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def quadrilateral_function():
    ConvexQuadrilateral('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def regularPentagon_function():
    regularPentagon = RegularPentagon('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def regularHexagon_function():
    regularHexagon = RegularHexagon('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


def regularOctagon_function():
    reguralOctagon = RegularOctagon('red', 'red')
    results_area = Label(root, text=f"Pole =\t{round(triangle.area(), 2)}").grid(column=10, row=0)
    results_perimeter = Label(root, text=f"Obwód =\t{round(triangle.perimeter(), 2)}").grid(column=10, row=1)


triangle = Button(root, text="Trójkąt", command=triangle_function).grid(column=0, row=0)
triangle1 = Button(root, text="Trójkąt Równoramienny", command=triangle1_function).grid(column=0, row=1)
triangle2 = Button(root, text="Trójkąt Równoboczny", command=triangle2_function).grid(column=0, row=2)
quadrilateral = Button(root, text="Dowolny Czworokąt", command=quadrilateral_function).grid(column=0, row=3)
regularPentagon = Button(root, text="Pięciokąt Foremny", command=regularPentagon_function).grid(column=0, row=4)
regularHexagon = Button(root, text="Sześciokąt Foremny", command=regularHexagon_function).grid(column=0, row=5)
reguralOctagog = Button(root, text="Ośmiokąt Foremny", command=regularOctagon_function).grid(column=0, row=6)
root.mainloop()