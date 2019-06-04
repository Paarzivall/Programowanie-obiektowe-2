from tkinter import *
import tkinter.ttk as ttk
from Triangle import Triangle
from IsoscelesTriangle import IsoscelesTriangle
from EquilateralTriangle import EquilateralTriangle
from ConvexQuadrilateral import ConvexQuadrilateral
from Parallelogram import Parallelogram
from Rhombus import Rhombus
from Square import Square
from Kite import Kite
from RegularPentagon import RegularPentagon
from RegularHexagon import RegularHexagon
from RegularOctagon import RegularOctagon


class Main(object):
    def __init__(self):
        self.root = Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}')
        self.root.configure(background="lightgray")
        self.canvas = Canvas(self.root, bg="white", width=screen_width/3, height=screen_height/2)
        self.canvas.place(x=250, y=20, height=500, width=600)
        self.draw_buttons()
        self.draw_pick_colors()
        self.draw_results()
        self.root.mainloop()

    def triangle_function(self):
        triangle = Triangle(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(triangle.area(),2)}\nObwód = {round(triangle.perimeter(), 2)}\nSkala = {triangle.skala}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)

    def triangle1_function(self):
        triangle = IsoscelesTriangle(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(triangle.area(), 2)}\nObwód = {round(triangle.perimeter(),2)}\nSkala = {triangle.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)

    def triangle2_function(self):
        triangle = EquilateralTriangle(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(triangle.area(), 2)}\nObwód = {round(triangle.perimeter(),2)}\nSkala = {triangle.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*triangle.draw(), fill=triangle.fill_colour, outline=triangle.outline_colour, width=6)

    def quadrilateral_function(self):
        quadrilateral = ConvexQuadrilateral(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(quadrilateral.area(),2)}\nObwód = {round(quadrilateral.perimeter(), 2)}\nSkala = {quadrilateral.skala}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*quadrilateral.draw(), fill=quadrilateral.fill_colour, outline=quadrilateral.outline_colour, width=6)

    def parallelogram_function(self):
        parallelogram = Parallelogram(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(parallelogram.area(), 2)}\nObwód = {round(parallelogram.perimeter(),2)}\nSkala = {parallelogram.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*parallelogram.draw(), fill=parallelogram.fill_colour, outline=parallelogram.outline_colour, width=6)

    def rhombus_function(self):
        rhombus = Rhombus(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(rhombus.area(), 2)}\nObwód = {round(rhombus.perimeter(),2)}\nSkala = {rhombus.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*rhombus.draw(), fill=rhombus.fill_colour, outline=rhombus.outline_colour, width=6)

    def square_function(self):
        square = Square(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(square.area(), 2)}\nObwód = {round(square.perimeter(),2)}\nSkala = {square.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*square.draw(), fill=square.fill_colour, outline=square.outline_colour, width=6)

    def kite_function(self):
        kite = Kite(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(kite.area(), 2)}\nObwód = {round(kite.perimeter(),2)}\nSkala = {kite.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*kite.draw(), fill=kite.fill_colour, outline=kite.outline_colour, width=6)

    def regularPentagon_function(self):
        regularPentagon = RegularPentagon(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(regularPentagon.area(),2)}\nObwód = {round(regularPentagon.perimeter(), 2)}\nSkala = {regularPentagon.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*regularPentagon.draw(), fill=regularPentagon.fill_colour, outline=regularPentagon.outline_colour, width=6)

    def regularHexagon_function(self):
        regularHexagon = RegularHexagon(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(regularHexagon.area(),2)}\nObwód = {round(regularHexagon.perimeter(), 2)}\nSkala = {regularHexagon.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*regularHexagon.draw(), fill=regularHexagon.fill_colour, outline=regularHexagon.outline_colour, width=6)

    def regularOctagon_function(self):
        reguralOctagon = RegularOctagon(str(self.color_value_back.get()), str(self.color_value_out.get()))
        self.results.config(text=f"Pole =\t{round(reguralOctagon.area(),2)}\nObwód = {round(reguralOctagon.perimeter(), 2)}\nSkala = {reguralOctagon.get_skala()}")
        self.canvas.delete("all")
        self.canvas.create_polygon(*reguralOctagon.draw(), fill=reguralOctagon.fill_colour, outline=reguralOctagon.outline_colour, width=6)

    def draw_buttons(self):
        triangle = Button(self.root, text="Trójkąt", command=self.triangle_function, width=25)
        triangle.place(x=20, y=20)

        triangle1 = Button(self.root, text="Trójkąt Równoramienny", command=self.triangle1_function, width=25)
        triangle1.place(x=20, y=50)

        triangle2 = Button(self.root, text="Trójkąt Równoboczny", command=self.triangle2_function, width=25)
        triangle2.place(x=20, y=80)

        quadrilateral = Button(self.root, text="Dowolny Czworokąt", command=self.quadrilateral_function, width=25)
        quadrilateral.place(x=20, y=110)

        parallelogram = Button(self.root, text="Równoległobok", command=self.parallelogram_function, width=25)
        parallelogram.place(x=20, y=140)

        rhombus = Button(self.root, text="Romb", command=self.rhombus_function, width=25)
        rhombus.place(x=20, y=170)

        square = Button(self.root, text="Kwadrat", command=self.square_function, width=25)
        square.place(x=20, y=200)

        kite = Button(self.root, text="Deltoid", command=self.kite_function, width=25)
        kite.place(x=20, y=230)

        regularPentagon = Button(self.root, text="Pięciokąt Foremny", command=self.regularPentagon_function, width=25)
        regularPentagon.place(x=20, y=260)

        regularHexagon = Button(self.root, text="Sześciokąt Foremny", command=self.regularHexagon_function, width=25)
        regularHexagon.place(x=20, y=290)

        reguralOctagon = Button(self.root, text="Ośmiokąt Foremny", command=self.regularOctagon_function, width=25)
        reguralOctagon.place(x=20, y=320)

    def draw_pick_colors(self):
        text1 = Label(self.root, text="Wybierz kolor wypełnienia: ")
        text1.place(x=20, y=350)
        text1.configure(background="lightgray")

        self.color_value_back = StringVar()
        combobox = ttk.Combobox(self.root, textvariable=self.color_value_back)
        combobox.place(x=20, y=370, width=185)
        combobox['values'] = ('blue', 'green', 'black', 'red', 'pink')
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>")

        text2 = Label(self.root, text="Wybierz kolor Obramowania: ")
        text2.place(x=20, y=395)
        text2.configure(background="lightgray")

        self.color_value_out = StringVar()
        combobox = ttk.Combobox(self.root, textvariable=self.color_value_out)
        combobox.place(x=20, y=415, width=185)
        combobox['values'] = ('blue', 'green', 'black', 'red', 'pink')
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>")

    def draw_results(self):
        self.results = Label(self.root, text=f"Pole =\nObwód =\nSkala =")
        self.results.place(x=30, y=450)
        self.results.configure(background="lightgray")


if __name__ == '__main__':
    m = Main()
