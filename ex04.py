'''Exercise 04 - Norm, and a main function to run tests'''

from complex import Complex
from vector import Vector


def main():
    '''Test case for exercise 04'''
    print("Results for exercise 04")

    u = Vector([0., 0., 0.])
    print(u.norm_1(), u.norm(), u.norm_inf())  # 0.0 0.0 0.0

    u = Vector([1., 2., 3.])
    print(u.norm_1(), u.norm(), u.norm_inf())  # 6.0 3.74165738 3.0

    u = Vector([-1., -2.])
    print(u.norm_1(), u.norm(), u.norm_inf())  # 3.0 2.236067977 2.0

    print("-- eval sheet extra cases --")
    for coords in ([0.], [1.], [0., 0.], [1., 0.], [2., 1.], [4., 2.], [-4., -2.]):
        v = Vector(coords)
        print(f"{coords}: norm_1={v.norm_1()} norm={v.norm()} norm_inf={v.norm_inf()}")

    print("-- K = Complex --")
    u = Vector([Complex(3., 4.)])
    print(u.norm_1(), u.norm(), u.norm_inf())  # 5.0 5.0 5.0 (norm relies on |z|=modulus)
    u = Vector([Complex(3., 4.), Complex(0., 1.)])
    print(u.norm_1(), u.norm(), u.norm_inf())  # 6.0 5.09901951 5.0


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
