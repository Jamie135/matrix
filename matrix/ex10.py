'''Exercise 10 - row-echelon form, and a main function to run tests'''

from matrix import Matrix


def main():
    '''Test case for exercise 10'''
    print("Results for exercise 10")

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

    print("-- eval sheet extra cases --")
    Matrix([[4., 2.], [2., 1.]]).row_echelon().print_matrix()  # [1, 0.5] [0, 0]
    Matrix([[-7., 2.], [4., 8.]]).row_echelon().print_matrix()  # [1, 0] [0, 1]
    Matrix([[1., 2.], [4., 8.]]).row_echelon().print_matrix()  # [1, 2] [0, 0]


if __name__ == "__main__":
    main()
