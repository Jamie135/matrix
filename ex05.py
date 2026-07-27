'''Exercise 05 - Cosine, and a main function to run tests'''

from typing import TypeVar
from complex import Complex
from vector import Vector

K = TypeVar("K")


def angle_cos(u: Vector[K], v: Vector[K]) -> float:
    '''cosine of the angle between u and v'''
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("argument is not of Vector type")
    if all(value == 0 for value in u.value) or all(value == 0 for value in v.value):
        raise ValueError("vector arguments are zero")
    # O(n) time complexity, O(1) space complexity (relies on dot/norm which are O(n))
    return u.dot(v) / (u.norm() * v.norm())


def main():
    '''Test case for exercise 05'''
    print("Results for exercise 05\n")

    print(angle_cos(Vector([1., 0.]), Vector([1., 0.])))    # 1.0
    print(angle_cos(Vector([1., 0.]), Vector([0., 1.])))    # 0.0
    print(angle_cos(Vector([-1., 1.]), Vector([1., -1.])))  # -1.0
    print(angle_cos(Vector([2., 1.]), Vector([4., 2.])))    # 1.0
    print(angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.])))  # 0.974631846

    print("\n-- eval sheet extra cases --\n")
    print(angle_cos(Vector([8., 7.]), Vector([3., 2.])))    # 0.9914542955425437
    print(angle_cos(Vector([1., 1.]), Vector([1., 1.])))    # 1
    print(angle_cos(Vector([4., 2.]), Vector([1., 1.])))    # 0.9486832980505138
    print(angle_cos(Vector([-7., 3.]), Vector([6., 4.])))   # -0.5462677805469223

    print("\n-- eval sheet: commutativity (order must not matter) --\n")
    for a, b in [([8., 7.], [3., 2.]), ([-7., 3.], [6., 4.])]:
        u, v = Vector(a), Vector(b)
        print(f"angle_cos(u, v) == angle_cos(v, u): {angle_cos(u, v) == angle_cos(v, u)}")

    print("\n-- K = Complex --\n")
    print(angle_cos(Vector([Complex(1.), Complex(0.)]), Vector([Complex(1.), Complex(0.)])))
    # 1.0
    print(angle_cos(Vector([Complex(1., 2.), Complex(3., -1.)]),
                     Vector([Complex(0., 1.), Complex(1., 1.)])))
    # (0.5962847939999439-0.74535599249993i)


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
