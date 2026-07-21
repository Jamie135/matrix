'''Exercise 14 - Bonus: Projection matrix, and a main function to run tests'''

from math import tan
from matrix import Matrix


def fma(a: float, b: float, c: float = 0.) -> float:
    '''custom fused multiply-add'''
    return (a * b) + c


def projection(fov: float, ratio: float, near: float, far: float) -> Matrix[float]:
    '''
    Build the camera-to-screen (projection) matrix for a perspective frustum.
    fov is expected in radians. Output is column-major, and targets Normalized
    Device Coordinates in [-1, 1] for x/y and [0, 1] for z, matching the
    display tool's convention (see subject XX.0.2).
    '''
    if fov <= 0 or ratio <= 0 or near <= 0 or far <= near:
        raise ValueError("Invalid projection parameters")

    # focal length: how much the half field-of-view angle compresses x/y
    f: float = 1.0 / tan(fov / 2.0)
    range_inv: float = 1.0 / (near - far)

    # Matrix() takes a list of ROWS (it converts to column-major internally,
    # see matrix.py). This targets NDC z in [0, 1] and x/y in [-1, 1].
    return Matrix([
        [f / ratio, 0., 0., 0.],
        [0., f, 0., 0.],
        [0., 0., fma(far, range_inv, 0.), fma(far * near, range_inv, 0.)],
        [0., 0., -1., 0.],
    ])


def main():
    '''Test case for exercise 14'''
    print("Results for exercise 14")

    for degrees in (100., 70., 40.):
        radians = degrees * 3.14159265358979323846 / 180.0
        m = projection(radians, 1.0, 0.1, 100.0)
        print(f"-- fov={degrees} degrees --")
        m.print_matrix()

    print("-- ratio distortion --")
    projection(70. * 3.14159265358979323846 / 180.0, 16 / 9, 0.1, 100.0).print_matrix()

    print("Write the matrix to a file to feed the provided 'display' tool, e.g.:")
    print("  python3 -c \"from ex14 import projection; "
          "print('\\n'.join(', '.join(map(str, row)) for row in projection(...).value))\"")


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
