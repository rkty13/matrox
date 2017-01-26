from element import Element

class Fraction(Element):
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator of Fraction cannot be 0.")
        self._numerator = numerator
        self._denominator = denominator

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def __add__(self, y):
        return add_fractions(self, y)

    def __radd__(self, y):
        return add_fractions(self, y)

    def __iadd__(self, y):
        return add_fractions(self, y)

    def __sub__(self, y):
        return subtract_fractions(self, y)

    def __rsub__(self, y):
        return subtract_fractions(self, y)

    def __isub__(self, y):
        return subtract_fractions(self, y)

    def __mul__(self, y):
        return multiply_fractions(self, y)

    def __rmul__(self, y):
        return multiply_fractions(self, y)

    def __imul__(self, y):
        return multiply_fractions(self, y)

    def __truediv__(self, y):
        return divide_fractions(self, y)

    def __rtruediv__(self, y):
        return divide_fractions(y, self)

    def __itruediv__(self, y):
        return divide_fractions(self, y)

    def __str__(self):
        if self._numerator == 0:
            return str(0)
        if self._denominator == 1:
            return str(self._numerator)
        return "/".join((str(self._numerator), str(self._denominator)))

    def __repr__(self):
        return self.__str__()



def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def simplify_fraction(fraction):
    div = gcd(fraction.get_numerator(), fraction.get_denominator())
    return Fraction(int(fraction.get_numerator() / div), 
                    int(fraction.get_denominator() / div))

def add_fractions(fraction_a, fraction_b, simplify=True):
    if type(fraction_a) in (int, float):
        fraction_a = Fraction(fraction_a)
    elif type(fraction_a) is Fraction:
        pass
    else:
        raise ValueError("fraction_a must be of type int, float, or Fraction.")

    if type(fraction_b) in (int, float):
        fraction_b = Fraction(fraction_b)
    elif type(fraction_b) is Fraction:
        pass
    else:
        raise ValueError("fraction_b must be of type int, float, or Fraction.")

    result = Fraction(
                fraction_a.get_numerator() * fraction_b.get_denominator() +
                fraction_b.get_numerator() * fraction_a.get_denominator(),
                fraction_a.get_denominator() * fraction_b.get_denominator()
            )
    return simplify_fraction(result) if simplify else result

def multiply_fractions(fraction_a, fraction_b, simplify=True):
    if type(fraction_a) in (int, float):
        fraction_a = Fraction(fraction_a)
    elif type(fraction_a) is Fraction:
        pass
    else:
        raise ValueError("fraction_a must be of type int, float, or Fraction.")

    if type(fraction_b) in (int, float):
        fraction_b = Fraction(fraction_b)
    elif type(fraction_b) is Fraction:
        pass
    else:
        raise ValueError("fraction_b must be of type int, float, or Fraction.")
    
    result = Fraction(fraction_a.get_numerator() * fraction_b.get_numerator(),
                    fraction_b.get_denominator() * fraction_b.get_denominator())

    return simplify_fraction(result) if simplify else result

def subtract_fractions(fraction_a, fraction_b, simplify=True):
    negated = multiply_fractions(fraction_b, -1)
    return add_fractions(fraction_a, negated, simplify=simplify)

def divide_fractions(fraction_a, fraction_b, simplify=True):
    reciprocal = Fraction(fraction_b.get_denominator(), 
                            fraction_b.get_numerator())
    return multiply_fractions(fraction_a, reciprocal, simplify=simplify)
