# Work with Ittiwat
class Complex:
    """
    This class will support complex number in python
    """
    def __init__(self, re=0, im=0):
        """
        Complex has 2 float attributes
        :param re: real part
        :param im: imaginary part
        """
        self.re = float(re)
        self.im = float(im)

    def __str__(self):
        """
        To present complex class as string
        :return: Complex number
        """
        if self.im < 0:
            return f"({self.re} {'-'} {abs(self.im)}i)"
        else:
            return f"({self.re} {'+'} {abs(self.im)}i)"

    def __repr__(self):
        """
        To present complex class as string
        :return: Complex number
        """
        if self.im >= 0:
            return f"({self.re} {'+'} {self.im}i)"
        else:
            return f"({self.re} {'-'} {self.im}i)"

    #  Problem 3 Arithmetic
    def __add__(self, other):
        """
        Method for adding
        :param other:
        :return: The sum of complex number
        """
        if type(other) == Complex:
            return Complex(self.re + other.re, self.im + other.im)
        else:
            return Complex(self.re + other, self.im)

    def __radd__(self, other):
        """
        Method for adding
        :param other:
        :return: The sum of complex number
        """
        if type == Complex:
            return Complex(self.re + other.re, self.im + other.im)
        else:
            return Complex(self.re + other, self.im)

    def __mul__(self, other):
        """
        Method for multiplication
        :param other:
        :return: The product of complex number
        """
        if type(other) == Complex:
            return Complex(self.re * other.re, self.im * other.im)
        else:
            return Complex(self.re * other, self.im * other)

    def __rmul__(self, other):
        """
        Method for multiplication
        :param other:
        :return: The product of complex number
        """
        if type == Complex:
            return Complex(self.re * other.re, self.im * other.im)
        else:
            return Complex(self.re * other, self.im * other)


if __name__ == '__main__':
    a = Complex(2.0, 3.0)
    print(a + Complex(-1.5, 2))  # (0.5 + 5.0i)
    print(a + 8)  # (10.0 + 3.0i)
    print(3.5 + a)  # (5.5 + 3.0i)
    a = Complex(1.0, -3.0)
    print(a * Complex(4.0, 5.5))  # (20.5 - 6.5i) Wrong
    print(a * 3.5)  # (3.5 - 10.5i)
    print(-2 * a)  # (-2.0 + 6.0i)
