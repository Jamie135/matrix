'''Exercise 03 - Dot product, and a main function to run tests'''

from vector import Vector


def main():
    '''Test case for exercise 03'''
    print("Results for exercise 03")

    print(Vector([0., 0.]).dot(Vector([1., 1.])))   # 0.0
    print(Vector([1., 1.]).dot(Vector([1., 1.])))   # 2.0
    print(Vector([-1., 6.]).dot(Vector([3., 2.])))  # 9.0

    print("-- eval sheet extra cases --")
    print(Vector([1., 0.]).dot(Vector([0., 0.])))  # 0
    print(Vector([1., 0.]).dot(Vector([1., 0.])))  # 1
    print(Vector([1., 0.]).dot(Vector([0., 1.])))  # 0
    print(Vector([4., 2.]).dot(Vector([2., 1.])))  # 10


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
