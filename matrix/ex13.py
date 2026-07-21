'''Exercise 13 - Rank, and a main function to run tests'''

from matrix import Matrix


def main():
    '''Test case for exercise 13'''
    print("Results for exercise 13")

    print(Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]).rank())  # 3
    print(Matrix([[1., 2., 0., 0.], [2., 4., 0., 0.], [-1., 2., 1., 1.]]).rank())  # 2
    print(Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.],
    ]).rank())  # 3

    print("-- eval sheet extra cases --")
    print(Matrix([[0., 0.], [0., 0.]]).rank())  # 0
    print(Matrix([[1., 0.], [0., 1.]]).rank())  # 2
    print(Matrix([[2., 0.], [0., 2.]]).rank())  # 2
    print(Matrix([[1., 1.], [1., 1.]]).rank())  # 1
    print(Matrix([[0., 1.], [1., 0.]]).rank())  # 2
    print(Matrix([[1., 2.], [3., 4.]]).rank())  # 2
    print(Matrix([[-7., 5.], [4., 6.]]).rank())  # 2


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
