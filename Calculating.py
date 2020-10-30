from Calculate_area import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle_1 = Circle(5)
circle_2 = Circle(10)
print(circle_1.get_area_circle())
print(circle_2.get_area_circle())
