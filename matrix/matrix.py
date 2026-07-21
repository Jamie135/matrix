'''
matrix class definition and methods.
K is an unconstrained generic (see ex15 bonus): int, float or Complex.
Values are stored internally in a single flat, column-major list.
'''
from typing import Generic, TypeVar, cast
from vector import Vector

K = TypeVar("K")


class Matrix(Generic[K]):
    '''Matrix class'''

    def __init__(self, value: list[list[K]]):
        self._check_matrix(value)
        self._record_shape(value)
        # insert argument into 1D column-major array
        self._value: list[K] = [value[j][i] for i, _ in enumerate(value[0])
                                 for j in range(len(value))]

    def _check_matrix(self, value: list[list[K]]):
        '''check argument values'''
        if len(value) == 0 or any(not isinstance(sublist, list) for sublist in value) or \
                any(len(sublist) == 0 for sublist in value) or \
                any(len(sublist) != len(value[0]) for sublist in value):
            raise TypeError("Invalid Matrix Form")

    def _record_shape(self, value: list[list[K]]):
        '''record shape of matrix in form (row, total element)'''
        self._shape: tuple = tuple([len(value),
                                    len([element for sublist in value for element in sublist])])

    @property
    def value(self) -> list[K]:
        '''getter for self._value'''
        return self._value

    @value.setter
    def value(self, new_value):
        '''setter for self._value'''
        self._value = new_value

    def size(self) -> tuple[int, int]:
        '''Utility function. Returns size of matrix in form (row count, element count)'''
        return self._shape

    def is_square(self) -> bool:
        '''Utility function. Returns True if the matrix is square'''
        column: int = self.size()[1] // self.size()[0]
        return column == self.size()[0]

    def print_matrix(self):
        '''Utility function. Print matrix values'''
        for i in range(self.size()[0]):
            print([self.value[j] for j in range(i, len(self.value), self.size()[0])])

    # exercise 00
    def add(self, v: 'Matrix[K]'):
        '''Add operation for matrix'''
        # O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("matrix not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("matrix not of same type")
        for i, _ in enumerate(self.value):
            self.value[i] += v.value[i]

    def sub(self, v: 'Matrix[K]'):
        '''Subtract operation for matrix'''
        # O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("matrix not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("matrix not of same type")
        for i, _ in enumerate(self.value):
            self.value[i] -= v.value[i]

    def scl(self, a: K):
        '''Scale operation for matrix'''
        # O(n) time complexity and O(1) space complexity
        for i, _ in enumerate(self.value):
            self.value[i] *= a

    # exercise 07
    def mul_vec(self, vec: Vector[K]) -> Vector[K]:
        '''Matrix-vector multiplication. Max time complexity O(nm), space O(nm)'''
        column: int = self._shape[1] // self._shape[0]
        if vec.size() != column:
            raise ValueError("Argument vector size incorrect")
        result: list[K] = []
        for i in range(self.size()[0]):
            temp_result: K = 0
            for j in range(i, self.size()[1], self.size()[0]):
                temp_result += self.value[j] * vec.value[j // self.size()[0]]
            result.append(temp_result)
        return Vector(result)

    def mul_mat(self, mat: 'Matrix[K]') -> 'Matrix[K]':
        '''Matrix-matrix multiplication. Max time complexity O(nmp), space O(nm+mp+np)'''
        column: int = self._shape[1] // self._shape[0]
        if mat.size()[0] != column:
            raise ValueError("Argument matrix size incorrect")
        result: list[K] = []
        for i in range(mat.size()[1] // mat.size()[0]):
            for j in range(self.size()[0]):
                temp_result: K = 0
                for k in range(j, self.size()[1], self.size()[0]):
                    temp_result += self.value[k] * \
                        mat.value[(k // self.size()[0]) + (i * mat.size()[0])]
                result.append(temp_result)
        self._shape = (self.size()[0], len(result))
        self._value = result
        return self

    # exercise 08
    def trace(self) -> K:
        '''return trace of matrix'''
        column: int = self.size()[1] // self.size()[0]
        if column != self.size()[0]:
            raise TypeError("Can't return trace of a non-square matrix")
        result: K = 0
        # O(n) time complexity
        for i in range(column):
            result += self.value[(i * self.size()[0]) + i]
        return result

    # exercise 09
    def transpose(self) -> 'Matrix[K]':
        '''returns transpose of matrix'''
        outer_list: list[list[K]] = []
        column: int = self.size()[1] // self.size()[0]
        # O(nm) time complexity and O(nm) space complexity
        for i in range(column):
            inner_list: list[K] = []
            for j in range(self.size()[0]):
                inner_list.append(self.value[(i * self.size()[0]) + j])
            outer_list.append(inner_list)
        return Matrix(outer_list)

    # exercise 10
    def row_echelon(self) -> 'Matrix[K]':
        '''return matrix converted to reduced row echelon form'''

        def normalize_row(row):
            normalized: list[K] = []
            column: int | None = None
            for j in range(row, self.size()[1], self.size()[0]):
                denom: K = self.value[j]
                if denom == 0:
                    normalized.append(denom)
                    continue
                for k in range(j, self.size()[1], self.size()[0]):
                    self.value[k] /= denom  # type: ignore
                    if column is None:
                        column = len(normalized)
                    normalized.append(self.value[k])
                break
            return (column, normalized)

        def pivot(row, column, normalized):
            for j in range(0, self.size()[0]):
                if row == j:
                    continue
                elif self.value[column * self.size()[0] + j] == 0:
                    continue
                else:
                    count: int = column
                    deduct = self.value[column * self.size()[0] + j] * normalized[column]
                    for k in range(column * self.size()[0] + j, self.size()[1], self.size()[0]):
                        self.value[k] -= deduct * normalized[count]
                        count += 1

        # total time complexity is 2 * (m x n) hence O(n^2), space complexity O(1)
        for row in range(self.size()[0]):
            column, normalized = normalize_row(row)
            if column is not None:
                pivot(row, column, normalized)
        return self

    # exercise 11
    def determinant(self) -> K:
        '''return determinant of matrix (scalar value), via LU decomposition'''
        column: int = self.size()[1] // self.size()[0]
        row_swap: int = 1

        if column != self.size()[0]:
            raise TypeError("Can't return determinant of a non-square matrix")

        def swap_row(last, j):
            nonlocal row_swap
            for i in range(column):
                self.value[i * self.size()[0] + self.size()[0] - 1] = self.value[i * self.size()[0] + j]
                self.value[i * self.size()[0] + j] = last[i]
            row_swap *= -1

        # row operations below pivot to get upper triangular matrix, O(n^3)
        for i in range(column):
            for j in range(self.size()[0]):
                if j == i and self.value[i * self.size()[0] + j] != 0:
                    placeholder_row: int = j
                elif j == i and self.value[i * self.size()[0] + j] == 0:
                    last_swap: list[K] = [self.value[k] for k in
                                           range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    swap_row(last_swap, j)
                    break
                if j > i and self.value[i * self.size()[0] + j] != 0:
                    deduct: K = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + placeholder_row]  # type: ignore
                    column_placeholder: int = 0
                    for k in range(j, self.size()[1], self.size()[0]):
                        self.value[k] -= deduct * self.value[column_placeholder * self.size()[0] + placeholder_row]
                        column_placeholder += 1

        result: K | None = None
        # multiply diagonal of upper triangular matrix, O(n^2)
        for i in range(column):
            for j in range(self.size()[0]):
                if i == j:
                    if result is None:
                        result = self.value[i * self.size()[0] + j]
                    else:
                        result *= self.value[i * self.size()[0] + j]
        if result == 0:
            return result
        return row_swap * cast(K, result)

    # exercise 12
    def inverse(self) -> "Matrix[K]":
        '''return the inverse matrix, via Gauss-Jordan elimination on [A | I]'''
        copy: list[K] = self.value.copy()
        if self.determinant() == 0:
            raise TypeError("Determinant is zero. No inverse possible.")
        self.value = copy
        column: int = self.size()[1] // self.size()[0]
        identity: list[K] = []
        for i in range(column):
            for j in range(self.size()[0]):
                identity.append(1 if i == j else 0)

        def swap_row(last, last_swap_identity, j):
            for i in range(column):
                self.value[i * self.size()[0] + self.size()[0] - 1] = self.value[i * self.size()[0] + j]
                self.value[i * self.size()[0] + j] = last[i]
                identity[i * self.size()[0] + self.size()[0] - 1] = identity[i * self.size()[0] + j]
                identity[i * self.size()[0] + j] = last_swap_identity[i]

        # 1) lower triangular elimination, O(n^3)
        for i in range(column):
            for j in range(self.size()[0]):
                deduct_lower: K | None = None
                if i == j and self.value[i * self.size()[0] + j] != 0:
                    pivot: int = j
                elif i == j and self.value[i * self.size()[0] + j] == 0:
                    last_swap: list[K] = [self.value[k] for k in
                                          range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    last_swap_identity: list[K] = [identity[k] for k in
                                                   range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    swap_row(last_swap, last_swap_identity, j)
                    break
                if j != i and j > i and self.value[i * self.size()[0] + j] != 0:
                    if deduct_lower is None:
                        deduct_lower = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + pivot]  # type: ignore
                    column_placeholder: int = 0
                    for k in range(j, self.size()[1], self.size()[0]):
                        if deduct_lower is not None:
                            self.value[k] -= deduct_lower * self.value[column_placeholder * self.size()[0] + pivot]
                            identity[k] -= deduct_lower * identity[column_placeholder * self.size()[0] + pivot]
                        column_placeholder += 1

        # 2) upper triangular elimination, O(n^3)
        for i in range(column - 1, 0 - 1, -1):
            for j in range(self.size()[0] - 1, 0 - 1, -1):
                deduct_upper: K | None = None
                if i == j and self.value[i * self.size()[0] + j] != 0:
                    pivot_upper: int = j
                if j != i and j < i and self.value[i * self.size()[0] + j] != 0:
                    if deduct_upper is None:
                        deduct_upper = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + pivot_upper]  # type: ignore
                    column_placeholder_upper: int = column - 1
                    for k in range((column - 1) * self.size()[0] + j, 0 - 1, -self.size()[0]):
                        if deduct_upper is not None:
                            self.value[k] -= deduct_upper * self.value[column_placeholder_upper * self.size()[0] + pivot_upper]  # type: ignore
                            identity[k] -= deduct_upper * identity[column_placeholder_upper * self.size()[0] + pivot_upper]  # type: ignore
                        column_placeholder_upper -= 1

        # 3) normalize pivots, O(n^3)
        for i in range(column):
            for j in range(self.size()[0]):
                deduct_normalized: K | None = None
                if i == j:
                    if deduct_normalized is None:
                        deduct_normalized = self.value[i * self.size()[0] + j]
                    column_placeholder_normalized: int = 0
                    for k in range(j, self.size()[1], self.size()[0]):
                        if deduct_normalized is not None:
                            self.value[k] /= deduct_normalized  # type: ignore
                            identity[k] /= deduct_normalized  # type: ignore
                        column_placeholder_normalized += 1
        # total: O(n^2) + 3*O(n^3) => O(n^3) time, O(n^2) space
        self.value = identity
        return self

    # exercise 13
    def rank(self) -> int:
        '''return the rank of the matrix (number of independent rows/columns)'''
        self.row_echelon()

        def check_zero_row() -> int:
            zero_row: int = 0
            for j in range(self.size()[0]):
                if all(self.value[k] == 0 for k in range(j, self.size()[1], self.size()[0])):
                    zero_row += 1
            return zero_row
        return self.size()[0] - check_zero_row()


def reshape_vector_to_matrix(v: list[Vector[K]]) -> "Matrix[K]":
    '''reshape a list of vectors into a matrix (one vector per column)'''
    if not isinstance(v, list) or len(v) == 0 or \
            any(not isinstance(vector, Vector) for vector in v) \
            or any(vector.size() != v[0].size() for vector in v):
        raise ValueError("Vector argument incorrect")
    return Matrix([[v[j].value[i] for j, _ in enumerate(v)] for i in range(v[0].size())])
