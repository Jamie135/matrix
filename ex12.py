'''Exercise 12 - Inverse, and a main function to run tests'''

from complex import Complex
from matrix import Matrix


def main():
    '''Test case for exercise 12'''
    print("Results for exercise 12")

    Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).inverse().print_matrix()
    # identity, unchanged

    Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]).inverse().print_matrix()
    # [0.5, 0.0, 0.0] [0.0, 0.5, 0.0] [0.0, 0.0, 0.5]

    Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]).inverse().print_matrix()
    # [0.649425287, 0.097701149, -0.655172414]
    # [-0.781609195, -0.126436782, 0.965517241]
    # [0.143678161, 0.074712644, -0.206896552]

    print("-- eval sheet extra cases --")
    Matrix([[1., 0.], [0., 1.]]).inverse().print_matrix()  # [1, 0] [0, 1]
    Matrix([[2., 0.], [0., 2.]]).inverse().print_matrix()  # [0.5, 0] [0, 0.5]
    Matrix([[0.5, 0.], [0., 0.5]]).inverse().print_matrix()  # [2, 0] [0, 2]
    Matrix([[0., 1.], [1., 0.]]).inverse().print_matrix()  # [0, 1] [1, 0]
    Matrix([[1., 2.], [3., 4.]]).inverse().print_matrix()  # [-2, 1] [1.5, -0.5]

    print("-- singular matrix raises --")
    try:
        Matrix([[1., 1.], [1., 1.]]).inverse()
    except TypeError as e:
        print(f"Error as expected: {e}")

    print("-- K = Complex --")
    i = Complex(0., 1.)
    Matrix([[Complex(1.), Complex(1.)], [Complex(0.), i]]).inverse().print_matrix()
    # [(1.0+0.0i), (0.0+1.0i)] [(0.0+0.0i), (0.0-1.0i)]
    Matrix([[Complex(1.), Complex(0.)], [Complex(0.), i]]).inverse().print_matrix()
    # [(1.0+0.0i), (0.0+0.0i)] [(0.0+0.0i), (0.0-1.0i)]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
