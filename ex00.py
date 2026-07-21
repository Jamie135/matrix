'''Exercise 00 - Add, Subtract and Scale, and a main function to run tests'''

from vector import Vector
from matrix import Matrix


def main():
    '''Test case for exercise 00'''
    print("Results for exercise 00")

    print("-- Vector add --")
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.add(v)
    u.print_vector()  # [7.0] [10.0]

    print("-- Vector sub --")
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.sub(v)
    u.print_vector()  # [-3.0] [-4.0]

    print("-- Vector scl --")
    u = Vector([2., 3.])
    u.scl(2.)
    u.print_vector()  # [4.0] [6.0]

    print("-- Matrix add --")
    m = Matrix([[1., 2.], [3., 4.]])
    n = Matrix([[7., 4.], [-2., 2.]])
    m.add(n)
    m.print_matrix()  # [8.0, 6.0] [1.0, 6.0]

    print("-- Matrix sub --")
    m = Matrix([[1., 2.], [3., 4.]])
    n = Matrix([[7., 4.], [-2., 2.]])
    m.sub(n)
    m.print_matrix()  # [-6.0, -2.0] [5.0, 2.0]

    print("-- Matrix scl --")
    m = Matrix([[1., 2.], [3., 4.]])
    m.scl(2.)
    m.print_matrix()  # [2.0, 4.0] [6.0, 8.0]

    print("-- eval sheet: Vector add --")
    for a, b in [
        ([0., 0.], [0., 0.]),
        ([1., 0.], [0., 1.]),
        ([1., 1.], [1., 1.]),
        ([21., 21.], [21., 21.]),
        ([-21., 21.], [21., -21.]),
        ([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
         [9., 8., 7., 6., 5., 4., 3., 2., 1., 0.]),
    ]:
        u = Vector(a)
        u.add(Vector(b))
        print(f"{a} + {b} = {u.value}")
        print()

    print("-- eval sheet: Vector sub --")
    for a, b in [
        ([0., 0.], [0., 0.]),
        ([1., 0.], [0., 1.]),
        ([1., 1.], [1., 1.]),
        ([21., 21.], [21., 21.]),
        ([-21., 21.], [21., -21.]),
        ([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.],
         [9., 8., 7., 6., 5., 4., 3., 2., 1., 0.]),
    ]:
        u = Vector(a)
        u.sub(Vector(b))
        print(f"{a} - {b} = {u.value}")
        print()

    print("-- eval sheet: Vector scl --")
    for a, scalar in [
        ([0., 0.], 1.),
        ([1., 0.], 1.),
        ([1., 1.], 2.),
        ([21., 21.], 2.),
        ([42., 42.], 0.5),
    ]:
        u = Vector(a)
        u.scl(scalar)
        print(f"{a} * {scalar} = {u.value}")
        print()

    print("-- eval sheet: Matrix add --")
    for a, b in [
        ([[0., 0.], [0., 0.]], [[0., 0.], [0., 0.]]),
        ([[1., 0.], [0., 1.]], [[0., 0.], [0., 0.]]),
        ([[1., 1.], [1., 1.]], [[1., 1.], [1., 1.]]),
        ([[21., 21.], [21., 21.]], [[21., 21.], [21., 21.]]),
    ]:
        m = Matrix(a)
        m.add(Matrix(b))
        print(f"{a} + {b} =")
        m.print_matrix()

    print("-- eval sheet: Matrix sub --")
    for a, b in [
        ([[0., 0.], [0., 0.]], [[0., 0.], [0., 0.]]),
        ([[1., 0.], [0., 1.]], [[0., 0.], [0., 0.]]),
        ([[1., 1.], [1., 1.]], [[1., 1.], [1., 1.]]),
        ([[21., 21.], [21., 21.]], [[21., 21.], [21., 21.]]),
    ]:
        m = Matrix(a)
        m.sub(Matrix(b))
        print(f"{a} - {b} =")
        m.print_matrix()

    print("-- eval sheet: Matrix scl --")
    for a, scalar in [
        ([[0., 0.], [0., 0.]], 0.),
        ([[1., 0.], [0., 1.]], 1.),
        ([[1., 2.], [3., 4.]], 2.),
        ([[21., 21.], [21., 21.]], 0.5),
    ]:
        m = Matrix(a)
        m.scl(scalar)
        print(f"{a} * {scalar} =")
        m.print_matrix()


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
