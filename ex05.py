'''Exercise 05 - Cosine, and a main function to run tests'''

from typing import TypeVar
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
    print("Results for exercise 05")

    print(angle_cos(Vector([1., 0.]), Vector([1., 0.])))    # 1.0
    print(angle_cos(Vector([1., 0.]), Vector([0., 1.])))    # 0.0
    print(angle_cos(Vector([-1., 1.]), Vector([1., -1.])))  # -1.0
    print(angle_cos(Vector([2., 1.]), Vector([4., 2.])))    # 1.0
    print(angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.])))  # 0.974631846

    print("-- eval sheet extra cases --")
    print(angle_cos(Vector([8., 7.]), Vector([3., 2.])))    # 0.9914542955425437
    print(angle_cos(Vector([1., 1.]), Vector([1., 1.])))    # 1
    print(angle_cos(Vector([4., 2.]), Vector([1., 1.])))    # 0.9486832980505138
    print(angle_cos(Vector([-7., 3.]), Vector([6., 4.])))   # -0.5462677805469223


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
