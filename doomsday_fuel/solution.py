from fractions import Fraction


def matrix_to_standard_form(m):
    std_m = []
    terminal_states = []
    size = len(m)

    # define terminal and non terminal states
    for i, row in enumerate(m):
        sum_row = sum(row)
        if (sum_row == 0):
            terminal_states.append(i)
        else:
            for j in range(size):
                row[j] = Fraction(row[j], sum_row)
    non_terminal_states = [i for i in range(
        size) if (i not in terminal_states)]

    # add top identity matrix
    for i in range(len(terminal_states)):
        identity_line = [0] * size
        identity_line[i] = 1
        std_m.append(identity_line)

    # add remaining matrix
    for i in non_terminal_states:
        rq_line = []
        for j in terminal_states + non_terminal_states:
            rq_line.append(m[i][j])
        std_m.append(rq_line)

    return std_m, terminal_states


def extract_r_submatrix(matrix, id_size):
    return [row[:id_size] for row in matrix[id_size:]]


def extract_q_submatrix(matrix, id_size):
    return [row[id_size:] for row in matrix[id_size:]]


def identity_matrix(size):
    matrix = []
    for i in range(size):
        row = [0] * size
        row[i] = Fraction(1, 1)
        matrix.append(row)
    return matrix


def multiply_matrices(a, b):
    res = []
    for i in range(len(a)):
        res.append([0] * len(b[0]))
        for j in range(len(b[0])):
            dot_prod = Fraction(0, 1)
            for k in range(len(b)):
                dot_prod += a[i][k] * b[k][j]
            res[i][j] = dot_prod
    return res


def substract_matrices(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matrix_minor(m, i, j):
    return [(row[:j] + row[j + 1:]) for row in (m[:i] + m[i + 1:])]


def matrix_determinant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for j in range(len(m)):
        determinant += ((-1) ** j) * m[0][j] * \
            matrix_determinant(matrix_minor(m, 0, j))
    return determinant


def inverse_matrix(m):
    determinant = matrix_determinant(m)
    if len(m) == 2:
        return [
            [m[1][1] / determinant, -1 * m[0][1] / determinant],
            [-1 * m[1][0] / determinant, m[0][0] / determinant]
        ]

    # compute matrix of cofactors
    # M^-1 = tCom(M) / det(M)
    cofactors = [[(-1) ** (i + j) / determinant * matrix_determinant(matrix_minor(m, i, j))
                  for j in range(len(m))] for i in range(len(m))]
    return transpose_matrix(cofactors)


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def lcm_array(arr):
    res = 1
    for i in range(len(arr)):
        res = lcm(res, arr[i])
    return res


def solution(m):
    std_m, terminal_states = matrix_to_standard_form(m)
    if (len(terminal_states) == 1):
        return [1, 1]
    r = extract_r_submatrix(std_m, len(terminal_states))
    q = extract_q_submatrix(std_m, len(terminal_states))
    f = inverse_matrix(substract_matrices(identity_matrix(len(q)), q))
    fr = multiply_matrices(f, r)
    denominator = lcm_array([frac.denominator for frac in fr[0]])
    res = [frac.numerator * denominator / frac.denominator for frac in fr[0]]
    res.append(denominator)
    return res
