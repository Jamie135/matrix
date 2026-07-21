'''
Complex number type. Implements the field operations (+, -, *, /) required
for Vector/Matrix to be usable with K = Complex, as asked in the ex15 bonus.
No math library is used: multiplication/division are implemented by hand
following the usual complex number algebra rules.
'''


class Complex:
    '''a + bi complex number'''

    def __init__(self, re: float = 0.0, im: float = 0.0):
        self.re: float = float(re)
        self.im: float = float(im)

    @staticmethod
    def _coerce(value) -> 'Complex':
        '''allow mixing Complex with plain int/float scalars'''
        if isinstance(value, Complex):
            return value
        if isinstance(value, (int, float)):
            return Complex(value, 0.0)
        raise TypeError("Cannot coerce value to Complex")

    def conjugate(self) -> 'Complex':
        '''a - bi'''
        return Complex(self.re, -self.im)

    def __add__(self, other) -> 'Complex':
        o = Complex._coerce(other)
        return Complex(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, other) -> 'Complex':
        o = Complex._coerce(other)
        return Complex(self.re - o.re, self.im - o.im)

    def __rsub__(self, other) -> 'Complex':
        return Complex._coerce(other) - self

    def __neg__(self) -> 'Complex':
        return Complex(-self.re, -self.im)

    def __mul__(self, other) -> 'Complex':
        o = Complex._coerce(other)
        # (a + bi) * (c + di) = (ac - bd) + (bc + ad)i
        return Complex(self.re * o.re - self.im * o.im,
                        self.im * o.re + self.re * o.im)
    __rmul__ = __mul__

    def __truediv__(self, other) -> 'Complex':
        o = Complex._coerce(other)
        # (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        denom = o.re * o.re + o.im * o.im
        if denom == 0:
            raise ZeroDivisionError("division by zero complex number")
        return Complex((self.re * o.re + self.im * o.im) / denom,
                        (self.im * o.re - self.re * o.im) / denom)

    def __rtruediv__(self, other) -> 'Complex':
        return Complex._coerce(other) / self

    def __abs__(self) -> float:
        '''modulus, used as the "magnitude" of a complex scalar for norms'''
        return (self.re * self.re + self.im * self.im) ** 0.5

    def __eq__(self, other) -> bool:
        try:
            o = Complex._coerce(other)
        except TypeError:
            return NotImplemented
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self) -> str:
        sign = '+' if self.im >= 0 else '-'
        return f"({self.re}{sign}{abs(self.im)}i)"
