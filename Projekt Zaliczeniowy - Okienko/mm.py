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
root.configure(background="lightgray")
canvas = Canvas(root, bg="white", width=screen_width/3, height=screen_height/2)
canvas.place(x=250, y=20, height=500, width=600)


def triangle_function():
    triangle = Triangle('red', 'red')
    results.config(text=f"Pole =\t{round(triangle.area(),2)}\nObwód = {round(triangle.perimeter(), 2)}\nSkala = {triangle.skala}")
    canvas.delete("all")
    canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)


def triangle1_function():
    triangle = IsoscelesTriangle('red', 'blue')
    results.config(text=f"Pole =\t{round(triangle.area(), 2)}\nObwód = {round(triangle.perimeter(),2)}\nSkala = {triangle.get_skala()}")
    canvas.delete("all")
    canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)


def triangle2_function():
    triangle = EquilateralTriangle('red', 'red')
    results.config(text=f"Pole =\t{round(triangle.area(), 2)}\nObwód = {round(triangle.perimeter(),2)}\nSkala = {triangle.get_skala()}")
    canvas.delete("all")
    canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)


def quadrilateral_function():
    quadrilateral = ConvexQuadrilateral('red', 'red')
    results.config(text=f"Pole =\t{round(quadrilateral.area(),2)}\nObwód = {round(quadrilateral.perimeter(), 2)}")


def regularPentagon_function():
    regularPentagon = RegularPentagon('red', 'red')
    results.config(text=f"Pole =\t{round(regularPentagon.area(),2)}\nObwód = {round(regularPentagon.perimeter(), 2)}\nSkala = {regularPentagon.skala}")
    canvas.delete("all")
    canvas.create_polygon(*regularPentagon.draw(), fill=regularPentagon.fill_colour, outline=regularPentagon.outline_colour, width=6)


def regularHexagon_function():
    regularHexagon = RegularHexagon('red', 'red')
    results.config(text=f"Pole =\t{round(regularHexagon.area(),2)}\nObwód = {round(regularHexagon.perimeter(), 2)}")


def regularOctagon_function():
    reguralOctagon = RegularOctagon('red', 'red')
    results.config(text=f"Pole =\t{round(reguralOctagon.area(),2)}\nObwód = {round(reguralOctagon.perimeter(), 2)}")


triangle = Button(root, text="Trójkąt", command=triangle_function)
triangle.place(x=60, y=20)
triangle1 = Button(root, text="Trójkąt Równoramienny", command=triangle1_function)
triangle1.place(x=20, y=50)
triangle2 = Button(root, text="Trójkąt Równoboczny", command=triangle2_function)
triangle2.place(x=25, y=80)
quadrilateral = Button(root, text="Dowolny Czworokąt", command=quadrilateral_function)
quadrilateral.place(x=30, y=110)
regularPentagon = Button(root, text="Pięciokąt Foremny", command=regularPentagon_function)
regularPentagon.place(x=33, y=140)
regularHexagon = Button(root, text="Sześciokąt Foremny", command=regularHexagon_function)
regularHexagon.place(x=29, y=170)
reguralOctagon = Button(root, text="Ośmiokąt Foremny", command=regularOctagon_function)
reguralOctagon.place(x=30, y=200)

results = Label(root, text=f"Pole =\nObwód =\nSkala =")
results.place(x=30, y=250)
results.configure(background="lightgray")

root.mainloop()