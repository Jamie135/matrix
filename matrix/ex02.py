'''Exercise 02 - Linear interpolation, and a main function to run tests'''

from typing import TypeVar, cast
from matrix import Matrix
from vector import Vector

V = TypeVar("V", bound=Vector | Matrix | int | float)


def lerp(u: V, v: V, t: float) -> V:
    '''linear interpolation between u and v'''
    return_value: V = u
    if not isinstance(u, type(v)):
        raise TypeError("first 2 arguments are not of same type")
    if isinstance(u, (Vector, Matrix)) and isinstance(v, (Vector, Matrix)):
        if u.size() != v.size():
            raise ValueError("arguments are not of same size")
        if not isinstance(u.value[0], type(v.value[0])):
            raise ValueError("arguments are not of same type")
        # time complexity O(n), space complexity O(1) (in place on u)
        for i, _ in enumerate(u.value):
            u.value[i] = (u.value[i] * (1 - t)) + (v.value[i] * t)
    elif isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return_value = cast(V, (u * (1 - t)) + (v * t))
    return return_value


def main():
    '''Test case for exercise 02'''
    print("Results for exercise 02")

    print(lerp(0., 1., 0.))    # 0.0
    print(lerp(0., 1., 1.))    # 1.0
    print(lerp(0., 1., 0.5))   # 0.5
    print(lerp(21., 42., 0.3))  # 27.3

    lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3).print_vector()  # [2.6] [1.3]

    lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5) \
        .print_matrix()  # [11.0, 5.5] [16.5, 22.0]

    print("-- eval sheet extra cases --")
    print(lerp(0., 42., 0.5))    # 21.0
    print(lerp(-42., 42., 0.5))  # 0.0
    lerp(Vector([-42., 42.]), Vector([42., -42.]), 0.5).print_vector()  # [0.0] [0.0]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
