'''Exercise 07 - Linear map, Matrix multiplication, and a main function to run tests'''

from complex import Complex
from vector import Vector
from matrix import Matrix


def main():
    '''Test case for exercise 07'''
    print("Results for exercise 07")

    print("-- mul_vec --")
    Matrix([[1., 0.], [0., 1.]]).mul_vec(Vector([4., 2.])).print_vector()  # [4.0] [2.0]
    Matrix([[2., 0.], [0., 2.]]).mul_vec(Vector([4., 2.])).print_vector()  # [8.0] [4.0]
    Matrix([[2., -2.], [-2., 2.]]).mul_vec(Vector([4., 2.])).print_vector()  # [4.0] [-4.0]

    print("-- mul_mat --")
    Matrix([[1., 0.], [0., 1.]]).mul_mat(Matrix([[1., 0.], [0., 1.]])).print_matrix()
    # [1.0, 0.0] [0.0, 1.0]
    Matrix([[1., 0.], [0., 1.]]).mul_mat(Matrix([[2., 1.], [4., 2.]])).print_matrix()
    # [2.0, 1.0] [4.0, 2.0]
    Matrix([[3., -5.], [6., 8.]]).mul_mat(Matrix([[2., 1.], [4., 2.]])).print_matrix()
    # [-14.0, -7.0] [44.0, 22.0]

    print("-- eval sheet extra cases --")
    Matrix([[0., 0.], [0., 0.]]).mul_vec(Vector([4., 2.])).print_vector()  # [0, 0]
    Matrix([[1., 1.], [1., 1.]]).mul_vec(Vector([4., 2.])).print_vector()  # [6, 6]
    Matrix([[2., 0.], [0., 2.]]).mul_vec(Vector([2., 1.])).print_vector()  # [4, 2]
    Matrix([[0.5, 0.], [0., 0.5]]).mul_vec(Vector([4., 2.])).print_vector()  # [2, 1]
    Matrix([[9, -4, 1], [3, 11, 2]]).mul_mat(Matrix([[2., 1.], [4., 2.], [1., 0.]])).print_matrix()
    Matrix([[9, -4, 1], [3, 11, 2], [1, 0, 0]]).mul_mat(Matrix([[2., 1., 0., 7], [4., 2., -5, -2], [1., 0., -1, 4]])).print_matrix()
    Matrix([[2., 1.], [1., 2.]]).mul_mat(Matrix([[2.], [4.]])).print_matrix()

    print("-- K = Complex --")
    i = Complex(0., 1.)
    Matrix([[Complex(1.), Complex(0.)], [Complex(0.), i]]) \
        .mul_vec(Vector([Complex(2.), Complex(1.)])).print_vector()  # [(2.0+0.0i)] [(0.0+1.0i)]
    Matrix([[Complex(1.), Complex(0.)], [Complex(0.), i]]) \
        .mul_mat(Matrix([[Complex(1., 1.), Complex(0.)], [Complex(0.), Complex(2.)]])) \
        .print_matrix()  # [(1.0+1.0i), (0.0+0.0i)] [(0.0+0.0i), (0.0+2.0i)]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
