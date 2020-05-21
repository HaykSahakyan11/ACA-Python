class RomanNumeral:
    def __init__(self, roman_num):
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
        return decimal_ans

    def addition(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_decimal() + roman_num
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_decimal() + roman_num.convert_to_decimal()
        else:
            try:
                return self.convert_to_decimal() + self.convert_to_decimal(roman_num)
            except:
                raise ValueError

    def multiplication(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_decimal() * roman_num
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_decimal() * roman_num.convert_to_decimal()
        else:
            try:
                return self.convert_to_decimal() * self.convert_to_decimal(roman_num)
            except:
                raise ValueError

    def subtraction(self, roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_decimal() - roman_num
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_decimal() - roman_num.convert_to_decimal()
        else:
            try:
                return self.convert_to_decimal() - self.convert_to_decimal(roman_num)
            except:
                raise ValueError

    def __add__(self, roman_num):
        return self.addition(roman_num)

    def __mul__(self, other):
        return self.multiplication(other)

    def __sub__(self, other):
        return self.subtraction(other)

    def __str__(self):
        return "Roman number: {} ".format(self.roman_num)


class Person:
    def __init__(self, name: str, last_name: str, age: int, gender, student: bool, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    def Greeting(self, second_person):
        # if isinstance(second_person,Person):
        if second_person.__class__.__name__ == self.__class__.__name__:
            print("Welcome dear {}".format(second_person.name))
        else:
            raise ValueError("{} is not {}".format(second_person, self.__class__.__name__))

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        return "My favorite num is {}".format(num1)


import math
from abc import ABC, abstractmethod


class Polygon(ABC):
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.length_of_edges = []

    def input_sides(self, *args):
        if self.getedges() != len(args):
            raise ValueError("Incorrect number of edges")
        self.length_of_edges = list(args)

    def getedges(self):
        return self.num_edges

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


class Rectangle(Quadrilateral):

    def __init__(self):
        Quadrilateral.__init__(self)

    def input_sides(self, a, b):
        if str(a).isdigit() and str(b).isdigit():
            self.length_of_edges = [a, b] * 2
        else:
            raise ValueError("Incorrect input")

    def area(self):
        edge1, edge2 = self.length_of_edges[0], self.length_of_edges[1]
        return edge1 * edge2


class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)

    def input_sides(self, a):
        if str(a).isdigit():
            self.length_of_edges = [a] * 4
        else:
            raise ValueError("Incorrect input")

    def area(self):
        return self.length_of_edges[0] ** 2


def problem_1_test():
    print("********* Problem1 *********")
    a = RomanNumeral("X")
    print(a)

    print(a.convert_to_decimal())
    print(a)

    b = "V"
    print(a.addition(b))

    print(a.addition("MMMDCXLIX"))

    c = RomanNumeral("M")
    print(a.addition(c))

    print(a + b)
    print(a + "V")
    print(a + c)

    print(a - b)
    print(a - "V")
    print(a - c)


def problem_2_test():
    print("\n\n********* Problem2 *********")
    a = Person("Name1", "Last_name1", 29, "male", True, 123)
    b = Person("Name2", "Last_name2", 30, "female", False, 456)

    print(a.name)

    a.Greeting(b)
    a.Goodbye()

    print(a.Favourite_num(5))
    print(a._Person__password)

    #h = ["AAAPerson"]
    #a.Greeting(h)

def problem_3_test():
    print("\n\n********* Problem3 *********")
    ### a = Polygon(4) -> Error. Can`t use class Polygon as it is ABC
    """ Quadrilateral """
    print("\n---------------")
    print("Quadrilateral")
    print("---------------")
    quad = Quadrilateral()
    print(quad.getedges(),"edges")
    quad.input_sides(4, 4, 4, 4)
    print(quad.perimeter(),"perimeter")
    print(quad.area(), "area")

    """ Rectangle """
    print("\n---------------")
    print("Rectangle")
    print("---------------")
    rect = Rectangle()
    print(rect.getedges(), "edges")
    # rect.input_sides(5,"a")
    # print(rect.area())
    rect.input_sides(5, 6)
    print(quad.perimeter(), "perimeter")
    print(rect.area(),"area")

    """ Square """
    print("\n---------------")
    print("Square")
    print("---------------")
    sqr = Square()
    print(sqr.getedges(), "edges")
    # sqr.input_sides("a")
    # print(sqr.area())
    sqr.input_sides(11)
    print(sqr.perimeter(), "perimeter")
    print(sqr.area(), "area")



if __name__ == "__main__":
    problem_1_test()
    problem_2_test()
    problem_3_test()





