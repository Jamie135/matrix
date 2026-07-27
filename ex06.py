'''Exercise 06 - Cross product, and a main function to run tests'''

from typing import TypeVar
from complex import Complex
from vector import Vector

K = TypeVar("K")


def cross_product(u: Vector[K], v: Vector[K]) -> Vector[K]:
    '''cross product of two 3-dimensional vectors'''
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("argument is not of Vector type")
    if u.size() != 3 or v.size() != 3:
        raise ValueError("vector arguments are not of 3 dimensions")
    # O(1) time and space complexity: fixed number of operations regardless of input
    result: list[K] = [
        (u.value[1] * v.value[2]) - (u.value[2] * v.value[1]),
        (u.value[2] * v.value[0]) - (u.value[0] * v.value[2]),
        (u.value[0] * v.value[1]) - (u.value[1] * v.value[0]),
    ]
    return Vector(result)


def main():
    '''Test case for exercise 06'''
    print("Results for exercise 06")

    cross_product(Vector([0., 0., 1.]), Vector([1., 0., 0.])).print_vector()
    # [0.0] [1.0] [0.0]
    cross_product(Vector([1., 2., 3.]), Vector([4., 5., 6.])).print_vector()
    # [-3.0] [6.0] [-3.0]
    cross_product(Vector([4., 2., -3.]), Vector([-2., -5., 16.])).print_vector()
    # [17.0] [-58.0] [-16.0]

    print("-- eval sheet extra cases --")
    print(cross_product(Vector([0., 0., 0.]), Vector([0., 0., 0.])).value)  # [0, 0, 0]
    print(cross_product(Vector([1., 0., 0.]), Vector([0., 0., 0.])).value)  # [0, 0, 0]
    print(cross_product(Vector([1., 0., 0.]), Vector([0., 1., 0.])).value)  # [0, 0, 1]
    print(cross_product(Vector([8., 7., -4.]), Vector([3., 2., 1.])).value)  # [15, -20, -5]
    print(cross_product(Vector([1., 1., 1.]), Vector([1., 1., 1.])).value)  # [0, 0, 0]

    print("-- K = Complex --")
    cross_product(
        Vector([Complex(0.), Complex(0.), Complex(1.)]),
        Vector([Complex(1.), Complex(0.), Complex(0.)]),
    ).print_vector()  # [(0.0+0.0i)] [(1.0+0.0i)] [(0.0+0.0i)]
    cross_product(
        Vector([Complex(1., 1.), Complex(0.), Complex(2.)]),
        Vector([Complex(0., 1.), Complex(1.), Complex(0.)]),
    ).print_vector()  # [(-2.0+0.0i)] [(0.0+2.0i)] [(1.0+1.0i)]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
