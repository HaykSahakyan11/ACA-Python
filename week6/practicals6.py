from math import pi

class Circle :
    def __init__(self,radius, color):
        assert isinstance(radius, int) or isinstance(radius, float) , "Radius must be a number"
        self.radius = radius

        assert type(color) == str, "Color must be a string"
        self.color = color




    def __str__(self):
        return "A {} circle with radius {}".format(self.color,self.radius)

    def area(self):
        area = pi * self.radius*self.radius
        return area


    def circumference (self):
        return 2 * pi * self.radius

    def __add__(self,other):
        if self.__class__.__name__ + other.__class__.__name__:

            return self.area() + other.area()
        else:
            raise ValueError ("Can add only circles")


class RomanNumeral:
    def __init__(self, roman_num):
        assert type(roman_num) == str , ValueError ("Incorect input {}".format(roman_num))
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
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
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

    def floor_division(self,roman_num):
        if isinstance(roman_num, int):
            return self.convert_to_roman(self.convert_to_decimal() / roman_num)
        if isinstance(roman_num, RomanNumeral):
            return self.convert_to_roman(self.convert_to_decimal() / roman_num.convert_to_decimal())
        else:
            try:
                return self.convert_to_roman(self.convert_to_decimal() / self.convert_to_decimal(roman_num))
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
        return "Roman number: {} ".format(self.roman_num)






