import abc

class Vector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __mul__(self, scalar):
        return

    @abc.abstractmethod
    def __rmul__(self, scalar):
        return

    @abc.abstractmethod
    def __imul__(self, scalar):
        return

    @abc.abstractmethod
    def __add__(self, right):
        return

    @abc.abstractmethod
    def __radd__(self, left):
        return

    @abc.abstractmethod
    def __iadd__(self, right):
        return



class VectorSpace(metaclass=abc.ABCMeta):
    def __init__(self, vector=None):
        self.vector = vector

    @abc.abstractmethod
    def zero_vector(self):
        return self.vector(self.n)
