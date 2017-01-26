from .element import Element

class Fraction(Element):
    def __init__(self, numerator, denominator=1):
        self._num = numerator
        self._den = denominator

    def get_num(self):
        return self._num

    def get_den(self):
        return self._den

    def __add__(self, y):
        return add_fractions(self, y)

    def __radd__(self, y):
        return add_fractions(self, y)

    # def __iadd__(self, y):
    #     return add_fractions(self, y)

    def __sub__(self, y):
        return subtract_fractions(self, y)

    def __rsub__(self, y):
        return subtract_fractions(self, y)

    # def __isub__(self, y):
    #     return subtract_fractions(self, y)

    def __mul__(self, y):
        return multiply_fractions(self, y)

    def __rmul__(self, y):
        return multiply_fractions(self, y)

    # def __imul__(self, y):
    #     return multiply_fractions(self, y)

    def __truediv__(self, y):
        return divide_fractions(self, y)

    def __rtruediv__(self, y):
        return divide_fractions(y, self)

    # def __itruediv__(self, y):
    #     return divide_fractions(self, y)

    def __str__(self):
        if self._num == 0:
            return str(0)
        if self._den == 1:
            return str(self._num)
        return "/".join((str(self._num), str(self._den)))

    def __repr__(self):
        return self.__str__()



def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def simplify_fraction(fraction):
    div = gcd(fraction.get_num(), fraction.get_den())
    return Fraction(int(fraction.get_num() / div), 
                    int(fraction.get_den() / div))

def add_fractions(frac_a, frac_b, simplify=True):
    result = Fraction(
                frac_a.get_num() * frac_b.get_den() +
                frac_b.get_num() * frac_a.get_den(),
                frac_a.get_den() * frac_b.get_den()
            )
    return simplify_fraction(result) if simplify else result

def multiply_fractions(frac_a, frac_b, simplify=True):
    result = Fraction(frac_a.get_num() * frac_b.get_num(),
                    frac_b.get_den() * frac_b.get_den())

    return simplify_fraction(result) if simplify else result

def subtract_fractions(frac_a, frac_b, simplify=True):
    negated = multiply_fractions(frac_b, -1)
    return add_fractions(frac_a, negated, simplify=simplify)

def divide_fractions(frac_a, frac_b, simplify=True):
    reciprocal = Fraction(frac_b.get_den(), 
                            frac_b.get_num())
    return multiply_fractions(frac_a, reciprocal, simplify=simplify)
