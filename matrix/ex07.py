'''Exercise 07 - Linear map, Matrix multiplication, and a main function to run tests'''

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
    Matrix([[0.5, 0.], [0., 0.5]]).mul_vec(Vector([4., 2.])).print_vector()  # [2, 1]


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
