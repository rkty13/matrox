class Vector(object):
    def __init__(self, length = 0, copy = None):
        if copy is not None:
            if type(copy) is not list and type(copy) is not Vector:
                raise TypeError("copy is not of type list or Vector.")

        self._v = []
        for m in range(len(copy) if copy else length):
            self._v.append(copy[m] if copy else 0)

    def append(self, x):
        self._v.append(x)

    def __getitem__(self, x):
        return self._v[x]

    def __setitem__(self, key, value):
        self._v[key] = value

    def __len__(self):
        return len(self._v)

    def __str__(self):
        return str(self._v)

    def __repr__(self):
        return self.__str__()