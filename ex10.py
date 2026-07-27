'''Exercise 10 - row-echelon form, and a main function to run tests'''

from complex import Complex
from matrix import Matrix


def main():
    '''Test case for exercise 10'''
    print("Results for exercise 10\n")

    Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).row_echelon().print_matrix()
    # identity, unchanged

    Matrix([[1., 2.], [3., 4.]]).row_echelon().print_matrix()
    # [1.0, 0.0] [0.0, 1.0]

    Matrix([[1., 2.], [2., 4.]]).row_echelon().print_matrix()
    # [1.0, 2.0] [0.0, 0.0]

    Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ]).row_echelon().print_matrix()
    # [1.0, 0.625, 0.0, 0.0, -12.1666667]
    # [0.0, 0.0, 1.0, 0.0, -3.6666667]
    # [0.0, 0.0, 0.0, 1.0, 29.5]

    print("-- eval sheet extra cases --\n")
    Matrix([[0., 0.], [0., 0.]]).row_echelon().print_matrix()  # [0, 0] [0, 0]
    Matrix([[4., 2.], [2., 1.]]).row_echelon().print_matrix()  # [1, 0.5] [0, 0]
    Matrix([[-7., 2.], [4., 8.]]).row_echelon().print_matrix()  # [1, 0] [0, 1]
    Matrix([[1., 2.], [4., 8.]]).row_echelon().print_matrix()  # [1, 2] [0, 0]

    print("-- K = Complex --\n")
    i = Complex(0., 1.)
    Matrix([[Complex(1.), Complex(0.)], [Complex(0.), i]]).row_echelon().print_matrix()
    Matrix([[Complex(2.), Complex(0., 1.)], [Complex(4.), Complex(0., 2.)]]) \
        .row_echelon().print_matrix()
    # [(1.0+0.0i), (0.0+0.5i)] [(0.0+0.0i), (0.0+0.0i)] -- second row is a multiple of the first


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
