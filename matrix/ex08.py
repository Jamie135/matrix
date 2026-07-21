'''Exercise 08 - Trace, and a main function to run tests'''

from matrix import Matrix


def main():
    '''Test case for exercise 08'''
    print("Results for exercise 08")

    print(Matrix([[1., 0.], [0., 1.]]).trace())  # 2.0
    print(Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]]).trace())  # 9.0
    print(Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]]).trace())  # -21.0

    print("-- eval sheet extra cases --")
    print(Matrix([[0., 0.], [0., 0.]]).trace())  # 0
    print(Matrix([[1., 2.], [3., 4.]]).trace())  # 5
    print(Matrix([[8., -7.], [4., 2.]]).trace())  # 10
    print(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).trace())  # 3


if __name__ == "__main__":
    main()
