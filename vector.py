'''
vector class definition and methods.
K is left as an unconstrained generic on purpose (see subject ex15): any of
int, float, or our own Complex type (complex.py) can be used, as long
as it supports +, -, *, /, ==, and abs().
'''

from typing import Generic, TypeVar

from complex import Complex

K = TypeVar("K")


def _conj(x: K) -> K:
    '''conjugate helper: no-op on reals, flips sign of imaginary part on Complex'''
    conjugate = getattr(x, "conjugate", None)
    return conjugate() if callable(conjugate) else x


def _to_real(x) -> float:
    '''extract the real component of a scalar (needed since norms must be real)'''
    return x.re if hasattr(x, "re") else float(x)


class Vector(Generic[K]):
    '''Vector class'''

    def __init__(self, value: list[K]):
        if len(value) == 0:
            raise ValueError("Empty list in Vector initialisation")
        if not isinstance(value, list):
            raise ValueError("Argument is not a list")
        if len(value) > 0 and not all(
                isinstance(value[i], (int, float, complex, Complex)) for i in range(len(value))):
            raise ValueError("Elements in argument are not of type int, float or complex")
        self._value: list[K] = list(value)

    @property
    def value(self) -> list[K]:
        '''class getter for _value'''
        return self._value

    def size(self) -> int:
        '''Utility function. Returns size of vector'''
        return len(self._value)

    def print_vector(self) -> None:
        '''Utility function. Print vector values'''
        for i in self._value:
            print([i])
        print()

    # exercise 00
    def add(self, v: 'Vector[K]'):
        '''addition operation for vector
        Time complexity O(n), space complexity O(1): the loop runs once per
        coordinate and every operation inside it is done in place.
        '''
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector not of same type")
        for i in range(self.size()):
            self._value[i] += v.value[i]

    def sub(self, v: 'Vector[K]'):
        '''subtraction operation for vector'''
        # O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector not of same type")
        for i in range(self.size()):
            self._value[i] -= v.value[i]

    def scl(self, a: K):
        '''scale operation for vector'''
        # O(n) time complexity and O(1) space complexity
        for i in range(self.size()):
            self._value[i] *= a

    # exercise 03
    def dot(self, v: 'Vector[K]') -> K:
        '''dot (inner) product. Uses the conjugate of v's coordinates so
        that this remains a proper sesquilinear inner product over Complex
        vector spaces (and is a no-op over the reals, see VII.1 of subject).
        '''
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector values not of same type")
        result: K = 0
        # O(n) time complexity and O(1) space complexity
        for i in range(self.size()):
            result += self._value[i] * _conj(v.value[i])
        return result

    # exercise 04
    def norm_1(self) -> float:
        '''Taxicab / Manhattan norm: sum of the magnitudes of the coordinates'''
        # O(n) time complexity and O(1) space complexity
        result: float = 0.0
        for i in self.value:
            result += abs(i)
        return result

    def norm(self) -> float:
        '''Euclidean norm: sqrt of the (real) inner product of the vector with itself'''
        # O(n) time complexity and O(1) space complexity
        result: float = _to_real(self.dot(self))
        return result ** 0.5

    def norm_inf(self) -> float:
        '''Supremum norm: magnitude of the largest coordinate'''
        # O(n) time complexity and O(1) space complexity
        return max(abs(value) for value in self.value)
