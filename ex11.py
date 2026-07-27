'''Exercise 11 - Determinant, and a main function to run tests'''

from complex import Complex
from matrix import Matrix


def main():
    '''Test case for exercise 11'''
    print("Results for exercise 11")

    print(Matrix([[1., -1.], [-1., 1.]]).determinant())  # 0.0
    print(Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]).determinant())  # 8.0
    print(Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]).determinant())  # -174.0
    print(Matrix([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.],
    ]).determinant())  # 1032

    print("-- eval sheet extra cases --")
    print(Matrix([[0., 0.], [0., 0.]]).determinant())  # 0
    print(Matrix([[1., 0.], [0., 1.]]).determinant())  # 1
    print(Matrix([[2., 0.], [0., 2.]]).determinant())  # 4
    print(Matrix([[1., 1.], [1., 1.]]).determinant())  # 0
    print(Matrix([[0., 1.], [1., 0.]]).determinant())  # -1
    print(Matrix([[1., 2.], [3., 4.]]).determinant())  # -2
    print(Matrix([[-7., 5.], [4., 6.]]).determinant())  # -62
    print(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).determinant())  # 1

    print("-- K = Complex --")
    i = Complex(0., 1.)
    print(Matrix([[Complex(1.), Complex(1.)], [Complex(0.), i]]).determinant())  # (0.0+1.0i)
    print(Matrix([[Complex(1., 2.), Complex(3., -1.)], [Complex(0., 1.), Complex(1., 1.)]])
          .determinant())  # (-2.0+0.0i)


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
