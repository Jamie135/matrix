'''Exercise 01 - Linear combination, and a main function to run tests'''

from typing import TypeVar
from vector import Vector

K = TypeVar("K")


def fma(a: K, b: K, c: K = 0) -> K:
    '''custom fused multiply-add'''
    return (a * b) + c


def linear_combination(u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    '''linear combination of the vectors in u scaled by the matching coefs'''
    if len(u) == 0 or len(coefs) == 0:
        raise ValueError("Argument list is empty")
    if len(u) != len(coefs):
        raise ValueError("length of argument list is different")
    if not all(vector.size() == u[0].size() for vector in u):
        raise ValueError("Vector size different in argument list")
    # time complexity O(m x n): m vectors, n coordinates each
    # space complexity O(n): result vector has n coordinates
    result: list[K] = []
    for i in range(u[0].size()):
        accumulator: K = 0
        for j, vector in enumerate(u):
            accumulator = fma(vector.value[i], coefs[j], accumulator)
        result.append(accumulator)
    return Vector(result)


def main():
    '''Test case for exercise 01'''
    print("Results for exercise 01")

    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    linear_combination([e1, e2, e3], [10., -2., 0.5]).print_vector()
    # [10.0] [-2.0] [0.5]

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    linear_combination([v1, v2], [10., -2.]).print_vector()
    # [10.0] [0.0] [230.0]

    print("-- eval sheet extra cases --")
    print(linear_combination([Vector([-42., 42.])], [-1.]).value)  # [42, -42]
    print(linear_combination(
        [Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.]).value)  # [0]
    print(linear_combination(
        [Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])],
        [1., -10., -1.]).value)  # [-62, -8]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
