from element import Element

class Fraction(Element):
    def __init__(self, num, den = 1):
        self._num = num
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be 0.")
        self._den = den

    def simplify(self):
        div = self._gcd(self._num, self._den)
        return Fraction(int(self._num / div), int(self._den / div))

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def _addition(self, x, y):
        if type(y) in (int, float):
            y = Fraction(y)
        if x._den != y._den:
            return Fraction(x._num * y._den + y._num * x._den, x._den * y._den)
        else:
            return Fraction(x._num + y._num, x._den).simplify()

    def _subtraction(self, x, y):
        t = self._multiplication(y, Fraction(-1))
        return self._addition(x, t)

    def _multiplication(self, x, y):
        if type(y) in (int, float):
            y = Fraction(y)
        return Fraction(x._num * y._num, x._den * y._den).simplify()

    def _division(self, x, y):
        if type(y) in (int, float):
            y = Fraction(y)
        if type(x) in (int, float):
            x = Fraction(x)
        t = Fraction(y._den, y._num)
        return self._multiplication(x, t)

    def _eval(self):
        return self._num / self._den

    def _less_than(self, x, y):
        if type(y) in (int, float):
            return x._eval() < y
        return x._eval() < y._eval()

    def _less_equal_to(self, x, y):
        return self._less_than(x, y) or self._equal_to(self, x, y)

    def _equal_to(self, x, y):
        if type(y) in (int, float):
            return x._eval() == y
        return x._eval() == y._eval()

    def _not_equal_to(self, x, y):
        return not self._equal_to(x, y)

    def _greater_than(self, x, y):
        if type(y) in (int, float):
            return x._eval() > y
        return x._eval() > y._eval()

    def _greater_equal_to(self, x, y):
        return self._greater_than(x, y) or self._equal_to(x, y)

    def __str__(self):
        if self._num == 0:
            return str(0)
        if self._den == 1:
            return str(self._num)
        return "/".join((str(self._num), str(self._den)))

    def __repr__(self):
        return self.__str__()

    def __add__(self, y):
        return self._addition(self, y)

    def __radd__(self, y):
        return self._addition(self, y)

    def __iadd__(self, y):
        return self + y

    def __sub__(self, y):
        return self._subtraction(self, y)

    def __rsub__(self, y):
        return self._subtraction(self, y)

    def __isub__(self, y):
        return self - y

    def __mul__(self, y):
        return self._multiplication(self, y)

    def __rmul__(self, y):
        return self._multiplication(self, y)

    def __imul__(self, y):
        return self * y

    def __truediv__(self, y):
        return self._division(self, y)

    def __rtruediv__(self, y):
        return self._division(y, self)

    def __itruediv__(self, y):
        return self / y

    def __lt__(self, y):
        return self._less_than(self, y)

    def __le__(self, y):
        return self._less_equal_to(self, y)

    def __eq__(self, y):
        return self._equal_to(self, y)

    def __ne__(self, y):
        return self._not_equal_to(self, y)

    def __gt__(self, y):
        return self._greater_than(self, y)

    def __ge__(self, y):
        return self._greater_equal_to(self, y)