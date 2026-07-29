'''Exercise 14 - Bonus: Projection matrix, and a main function to run tests'''

import sys
from math import tan
from matrix import Matrix


def fma(a: float, b: float, c: float = 0.) -> float:
    '''custom fused multiply-add'''
    return (a * b) + c


def projection(fov: float, ratio: float, near: float, far: float) -> Matrix[float]:
    '''
    Build the camera-to-screen (projection) matrix for a perspective frustum.
    fov is expected in radians. Output is column-major, and targets Normalized
    Device Coordinates in [-1, 1] for x/y/z, matching the display tool's
    convention (see subject XX.0.2).
    '''
    if fov <= 0 or ratio <= 0 or near <= 0 or far <= near:
        raise ValueError("Invalid projection parameters")

    # focal length: how much the half field-of-view angle compresses x/y
    f: float = 1.0 / tan(fov / 2.0)
    range_inv: float = 1.0 / (near - far)

    # Matrix() takes a list of ROWS (it converts to column-major internally,
    # see matrix.py). This targets NDC z in [-1, 1] and x/y in [-1, 1].
    return Matrix([
        [f / ratio, 0., 0., 0.],
        [0., f, 0., 0.],
        [0., 0., (far + near) / (near - far), (2. * far * near) / (near - far)],
        [0., 0., -1., 0.],
    ])


def write_proj(fov_deg: float, ratio: float, near: float, far: float, path: str) -> None:
    '''Write a projection matrix to a file in the format expected by the
    matrix_display tool (comma-separated rows).'''
    radians = fov_deg * 3.14159265358979323846 / 180.0
    m = projection(radians, ratio, near, far)
    row_count = m.size()[0]
    rows = [[m.value[j] for j in range(i, len(m.value), row_count)] for i in range(row_count)]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(", ".join(map(str, row)) for row in rows))
        f.write("\n")
    print(f"Wrote fov={fov_deg} ratio={ratio} near={near} far={far} to {path}")


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
    print("  python3 ex14.py 70 1.0 0.1 100.0 [output_path]")


if __name__ == "__main__":
    try:
        if len(sys.argv) >= 5:
            out_path = sys.argv[5] if len(sys.argv) >= 6 else "matrix_display/proj"
            write_proj(float(sys.argv[1]), float(sys.argv[2]),
                       float(sys.argv[3]), float(sys.argv[4]), out_path)
        else:
            main()
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
