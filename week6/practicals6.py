from math import pi
import numpy as np


class Circle:
    def __init__(self, radius, color):
        assert isinstance(radius, int) or isinstance(radius, float), "Radius must be a number"
        self.radius = radius

        assert type(color) == str, "Color must be a string"
        self.color = color

    def __str__(self):
        return "A {} circle with radius {}".format(self.color, self.radius)

    def area(self):
        return round(pi * self.radius * self.radius, 2)

    def circumference(self):
        return round(2 * pi * self.radius, 2)

    def __add__(self, other):
        if self.__class__.__name__ + other.__class__.__name__:

            return round((self.area() + other.area()), 2)
        else:
            raise ValueError("Can add only circles")


class RomanNumeral:
    def __init__(self, roman_num):
        assert type(roman_num) == str, ValueError("Incorect input {}".format(roman_num))
        self.roman_num = roman_num

    def roman_dictionary(self, key):
        roman_Dictioanry = {'M': "1000",
                            'D': "500",
                            'C': "100",
                            'L': "50",
                            'X': "10",
                            'V': "5",
                            'I': "1"}
        try:
            return int(roman_Dictioanry[key])
        except:
            raise KeyError

    def convert_to_roman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]

        syb = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]

        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def convert_to_decimal(self, new_roman=False):
        if new_roman == False:
            data = self.roman_num
        else:
            data = new_roman
        decimal_ans, prev_num = 0, 0
        size = len(data)
        for i in range(size - 1, -1, -1):
            decimal = self.roman_dictionary(data[i])  # int(roman_dictionary[data[i]])
            if decimal >= prev_num:
                decimal_ans += decimal
            else:
                decimal_ans -= decimal
            prev_num = decimal
        if self.convert_to_roman(decimal_ans) == data:
            return decimal_ans
        else:
            raise ValueError('Input is not a valid Roman numeral: {}'.format(data))

    def addition(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_roman(self.convert_to_decimal() + roman_num)
        if isinstance(roman_num, RomanNumeral):

            return self.convert_to_roman(self.convert_to_decimal() + roman_num.convert_to_decimal())
        else:
            try:
                return self.convert_to_roman(self.convert_to_decimal() + self.convert_to_decimal(roman_num))
            except:
                raise ValueError

    def multiplication(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_roman(self.convert_to_decimal() * roman_num)
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_roman(self.convert_to_decimal() * roman_num.convert_to_decimal())
        else:
            try:
                return self.convert_to_roman(self.convert_to_decimal() * self.convert_to_decimal(roman_num))
            except:
                raise ValueError

    def subtraction(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_roman(self.convert_to_decimal() - roman_num)
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_roman(self.convert_to_decimal() - roman_num.convert_to_decimal())
        else:
            try:
                return self.convert_to_roman(self.convert_to_decimal() - self.convert_to_decimal(roman_num))
            except:
                raise ValueError

    def floor_division(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_roman(self.convert_to_decimal() // roman_num)
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_roman(self.convert_to_decimal() // roman_num.convert_to_decimal())
        else:
            try:
                return self.convert_to_roman(self.convert_to_decimal() // self.convert_to_decimal(roman_num))
            except:
                raise ValueError

    def __add__(self, roman_num):
        return self.addition(roman_num)

    def __mul__(self, other):
        return self.multiplication(other)

    def __sub__(self, other):
        return self.subtraction(other)

    def __floordiv__(self, other):
        return self.floor_division(other)

    def __str__(self):
        return "{} ".format(self.roman_num)


class Person:
    def __init__(self, name: str, last_name: str, age: int, gender, student: bool, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    def Read_file(self, filename):
        try:
            file = open("{}.txt".format(filename), "r")
            print("All correct")
        except FileNotFoundError as err:
            print(err)
        except Exception as err:
            print(err)
        else:
            data = file.read()
            file.close()
            return data

    def Greeting(self, second_person):
        # if isinstance(second_person,Person):
        if second_person.__class__.__name__ == self.__class__.__name__:
            print("Welcome dear {}".format(second_person.name))
        else:
            raise ValueError("{} is not {}".format(second_person, self.__class__.__name__))

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        assert type(num1) == int or type(num1) == float, "Input is not a number!!"
        return "My favorite num is {}".format(num1)


import math
from abc import ABC, abstractmethod


class Polygon(ABC):
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.length_of_edges = []

    @abstractmethod
    def input_sides(self, *args):
        assert len(args) == self.getedges(), "Incorrect number of edges for {}".format(self.__class__.__name__)
        list_args = np.array(args)
        assert np.issubdtype(list_args.dtype, np.number), "Sides must be numeric"

        assert all(list_args > 0), "Sides must be positive numbers"
        self.length_of_edges = list(args)

    def getedges(self):
        return self.num_edges

    def get_length_of_sides(self):
        return self.length_of_edges

    def perimeter(self):
        return sum(self.length_of_edges)

    @abstractmethod
    def area(self):
        pass


class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)

    def area(self):
        try:
            DA, AB, BC, CD = self.length_of_edges
            a = float(input("What is angle between first two edges in degrees?"))
            area1 = 0.5 * AB * DA * math.sin(math.radians(a))
            Diagonal_length = ((DA ** 2) + (AB ** 2) - (2 * DA * AB * math.cos(math.radians(a)))) ** 0.5
            perim1_2 = (BC + CD + Diagonal_length) / 2
            area2 = (perim1_2 * (perim1_2 - BC) * (perim1_2 - CD) * (perim1_2 - Diagonal_length)) ** 0.5
            return area1 + area2
        except:
            raise ValueError("Incorrect value for angle!!!")

    def input_sides(self, *args):
        assert len(args) == 4, "Incorrect number of edges for {}".format(self.__class__.__name__)
        list_args = np.array(args)
        assert np.issubdtype(list_args.dtype, np.number), "Sides must be numeric"

        assert all(list_args > 0), "Sides must be positive numbers"
        self.length_of_edges = list(args)


class Rectangle(Quadrilateral):

    def __init__(self):
        Quadrilateral.__init__(self)

    def input_sides(self, *args):
        assert len(args) == 2, "Incorrect number of edges for {}".format(self.__class__.__name__)
        list_args = np.array(args)
        assert np.issubdtype(np.array(args).dtype, np.number), "Sides must be numeric"

        assert all(list_args > 0), "Sides must be positive numbers"
        self.length_of_edges = list(args) * 2

    def area(self):
        edge1, edge2 = self.length_of_edges[0], self.length_of_edges[1]
        return edge1 * edge2


class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)

    def input_sides(self, *args):
        assert len(args) == 1, "Incorrect number of edges for {}".format(self.__class__.__name__)
        list_args = np.array(args)
        assert np.issubdtype(list_args.dtype, np.number), "Sides must be numeric"

        assert all(list_args > 0), "Sides must be positive numbers"
        self.length_of_edges = list(args) * 4

    def area(self):
        return self.length_of_edges[0] ** 2


def problem_1_test():
    circle1 = Circle(10, "red")
    circle2 = Circle(5, "yellow")
    print(circle1)
    print(circle1.area())
    print(circle1.circumference())
    print(circle1 + circle2)


def problem_2_test():
    rom_1 = RomanNumeral("MIX")
    print(rom_1.convert_to_decimal())
    rom_2 = RomanNumeral("V")
    print(rom_2.convert_to_decimal())

    import operator
    funcs = [operator.add, operator.sub, operator.mul, operator.floordiv]
    funcs_ = ["+", "-", "*", "//"]
    for i in range(len(funcs)):
        print("------------------------")
        print(str(funcs[i]).split()[-1][:-1])
        print("------------------------")
        print("{0}{1} {2} = {3}".format(rom_1, funcs_[i], rom_2, funcs[i](rom_1, rom_2)))
        print("{0}{1} {2} = {3}".format(rom_1, funcs_[i], 2, funcs[i](rom_1, 2)))
        print("{0}{1} {2} = {3}".format(rom_1, funcs_[i], "I", funcs[i](rom_1, "I")))

        print("\n")


def problem_3_test():
    person1 = Person("Name1", "Last_name1", 29, "male", True, 123)
    person2 = Person("Name2", "Last_name2", 30, "female", False, 456)

    """Creating a new file to read it after."""
    data = [1, 2, 3, 4, 5]
    new_file = open("aaa.txt", "w")
    new_file.write(str(data))
    new_file.close()

    filename = "aaa"
    print(person1.Read_file(filename))
    person1.Read_file("hhhhh")
    person1.Greeting(person2)
    person1.Goodbye()
    print(person1.Favourite_num(7.7))


def problem_4_test():
    print("\nQuadrilateral___________")
    quad = Quadrilateral()
    print(quad.num_edges, "Number of edges")
    # quad.input_sides(4,5,6,6,"5") # -> error
    print(quad.perimeter(), "Perimeter")
    quad.input_sides(4, 5, 6, 6)
    print(quad.perimeter(), "Perimeter")
    print(quad.area(), "Area")

    print("\nRectangle___________")
    rect = Rectangle()
    print(rect.getedges(), "Number of edges")
    rect.input_sides(4, 5)
    print(rect.perimeter(), "Perimeter")
    print(rect.get_length_of_sides(), "Length of sides")
    print(rect.area(), "Area")

    print("\nSquare___________")
    squar = Square()
    print(squar.getedges(), "Number of edges")
    squar.input_sides(4)
    print(squar.perimeter(), "Perimeter")
    print(squar.get_length_of_sides(), "Length of sides")
    print(squar.area(), "Area")


if __name__ == "__main__":
    problem_1_test()
    problem_2_test()
    problem_3_test()
    problem_4_test()
