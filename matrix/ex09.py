'''Exercise 09 - Transpose, and a main function to run tests'''

from matrix import Matrix


def main():
    '''Test case for exercise 09'''
    print("Results for exercise 09")

    Matrix([[1., 0.], [0., 1.]]).transpose().print_matrix()  # [1.0, 0.0] [0.0, 1.0]
    Matrix([[1., 2.], [3., 4.]]).transpose().print_matrix()  # [1.0, 3.0] [2.0, 4.0]
    Matrix([[1., 2.], [3., 4.], [5., 6.]]).transpose().print_matrix()
    # [1.0, 3.0, 5.0] [2.0, 4.0, 6.0]

    print("-- eval sheet extra cases --")
    Matrix([[0., 0.], [0., 0.]]).transpose().print_matrix()  # [0, 0] [0, 0]
    Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).transpose().print_matrix()
    # identity, unchanged


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
