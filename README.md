# matrix

This project dives deep into Linear Algebra, which powers most of
the underlying algorithms in Machine Learning, Artificial Intelligence, Computer
Graphics and other Computer Science subject matters.

Topics and exercises included in the project:

1. Vector and Matrix operations (add, subtract, scale)
2. Linear combination
3. Linear interpolation
4. Dot product
5. Norm
6. Cosine of the angle between two vectors
7. Cross product
8. Matrix multiplication (linear map)
9. Trace
10. Matrix transpose
11. Row-echelon form
12. Determinant of a matrix
13. Inverse of a matrix
14. Rank of a matrix
15. Bonus: Projection matrix (used to render 3D scenes)
16. Bonus: Complex vector spaces (K = Complex instead of K = float)

Project is coded in Python and each exercise imposes a time and space complexity
limit on its operations. It uses Python's generics (Python 3.10+ syntax) so that
`Vector[K]` and `Matrix[K]` are not hardcoded to `float`: `K` is left unconstrained,
which is what allows the bonus (ex15) to reuse every prior exercise unmodified with
a hand-written `Complex` type instead of `float`.

## Structure

- `complex.py` — hand-rolled `Complex` field (+, -, *, /, conjugate, modulus),
  used only for the bonus.
- `vector.py` / `matrix.py` — the `Vector[K]` / `Matrix[K]` classes and their methods.
- `ex00.py` … `ex15.py` — the mandatory exercises, each with a `main()` that runs

## To run

Requires Python 3.10+ (for the `X | Y` generic type hints used throughout).

```
python3 <exercise_no>.py
```

Each exercise prints its test results to stdout so they can be checked against
the expected values from the subject/eval sheet (given in comments next to each
call).
