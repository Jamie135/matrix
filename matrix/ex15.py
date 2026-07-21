'''
Exercise 15 - Bonus: Complex vector spaces.

Since Vector[K] and Matrix[K] were written with K left as an unconstrained
generic (see vector.py / matrix.py), every exercise from 00 to 13 already
works unmodified when K is our Complex type instead of float: this file
re-runs a representative sample of them over Complex numbers to demonstrate
that genericity, rather than duplicating each exercise file.
'''

from complex import Complex
from vector import Vector
from matrix import Matrix
from ex01 import linear_combination
from ex02 import lerp
from ex05 import angle_cos
from ex06 import cross_product


def main():
    '''Test case for exercise 15'''
    print("Results for exercise 15 (K = Complex)")

    i = Complex(0., 1.)

    print("-- ex00: add/sub/scl --")
    u = Vector([Complex(1., 2.), Complex(3., -1.)])
    v = Vector([Complex(0., 1.), Complex(1., 1.)])
    u.add(v)
    u.print_vector()  # [(1.0+3.0i)] [(4.0+0.0i)]

    print("-- ex01: linear_combination --")
    e1 = Vector([Complex(1.), Complex(0.)])
    e2 = Vector([Complex(0.), Complex(1.)])
    linear_combination([e1, e2], [Complex(2., 1.), Complex(0., -1.)]).print_vector()
    # [(2.0+1.0i)] [(0.0-1.0i)]

    print("-- ex02: lerp --")
    lerp(Vector([Complex(0.), Complex(0.)]), Vector([Complex(2.), i]), 0.5).print_vector()
    # [(1.0+0.0i)] [(0.0+0.5i)]

    print("-- ex03: dot product (sesquilinear inner product) --")
    print(Vector([i]).dot(Vector([i])))  # (1.0+0.0i) -- real and non-negative

    print("-- ex04: norm (must stay real, even over Complex vectors) --")
    print(Vector([Complex(3., 4.)]).norm())  # 5.0

    print("-- ex05: angle_cos --")
    print(angle_cos(Vector([Complex(1.), Complex(0.)]), Vector([Complex(1.), Complex(0.)])))
    # 1.0

    print("-- ex06: cross_product --")
    cross_product(
        Vector([Complex(0.), Complex(0.), Complex(1.)]),
        Vector([Complex(1.), Complex(0.), Complex(0.)]),
    ).print_vector()  # [(0.0+0.0i)] [(1.0+0.0i)] [(0.0+0.0i)]

    print("-- ex07/08/09: matrix mul, trace, transpose --")
    m = Matrix([[Complex(1.), Complex(0.)], [Complex(0.), i]])
    m.mul_vec(Vector([Complex(2.), Complex(1.)])).print_vector()  # [(2.0+0.0i)] [(0.0+1.0i)]
    print(m.trace())  # (1.0+1.0i)
    m.transpose().print_matrix()

    print("-- ex11/12: determinant/inverse over Complex --")
    n = Matrix([[Complex(1.), Complex(1.)], [Complex(0.), i]])
    print(n.determinant())  # (0.0+1.0i)
    Matrix([[Complex(1.), Complex(1.)], [Complex(0.), i]]).inverse().print_matrix()

    print("-- ex13: rank over Complex --")
    print(Matrix([[Complex(1.), Complex(0.)], [Complex(0.), Complex(1.)]]).rank())  # 2


if __name__ == "__main__":
    main()
