"""
Implementation of a tropical key exchange protocol.
"""
from tropical_matrix import *
import math
import random

def get_identity_matrix(n):
    if n <= 1:
        raise ValueError("An identity matrix must have more than a singular entry.")
    identity_matrix = []
    for i in range(n):
        row = [math.inf] * n
        row[i] = 0
        identity_matrix.append(row)
    return TropicalMatrix(identity_matrix)

def generate_random_matrix(n, min_term, max_term):
    new_matrix = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = random.randint(min_term, max_term)
    return TropicalMatrix(new_matrix)

def generate_random_tropical_poly(max_degree, min_coefficient, max_coefficient):
    """
    Generates a random (non-constant) tropical polynomial up to a given degree.
    """
    coefficients = []
    for d in range(0, random.randint(1, max_degree) + 1):
        coefficients.append(random.randint(min_coefficient, max_coefficient))
    return coefficients

def evaluate_polynomial(tropical_matrix, coefficient_list):
    """
    Evaluates the polynomial (in list form) given a tropical matrix.
    """
    identity_matrix = get_identity_matrix(tropical_matrix.get_dimension())
    sum_list = []
    sum_list.append(identity_matrix.mult_scalar(coefficient_list[0]))
    for i in range(1, len(coefficient_list)):
        sum_list.append(tropical_matrix.mult_scalar(coefficient_list[i]))
    return get_minimum_sum(sum_list)

def get_minimum_sum(matrix_list):
    new_matrix = matrix_list[0]
    for matrix in matrix_list:
        new_matrix = new_matrix.add_tropical_matrix(matrix)
    return new_matrix

def get_polynomial_representation(coefficient_list):
    term_list = [str(coefficient_list[0])]
    for i in range(1, len(coefficient_list)):
        term_list.append(str(coefficient_list[i]) + "x^" + str(i))
    return " + ".join(term_list)

def generate_key(public_term, public_matrix_a, public_matrix_b, private_poly_a, private_poly_b):
    p_1A = evaluate_polynomial(public_matrix_a, private_poly_a)
    p_2B = evaluate_polynomial(public_matrix_b, private_poly_b)
    left_term = p_1A.mult_tropical_matrix(public_term)
    return left_term.mult_tropical_matrix(p_2B)

if __name__ == "__main__":
    p_1 = [2, 5, 3]
    p_2 = [0, 9, 0, 2, 5]

    A = TropicalMatrix([[3, 2], [1, -2]])
    B = TropicalMatrix([[7, 1], [2, -3]])
    p_1A = evaluate_polynomial(A, p_1)
    p_2B = evaluate_polynomial(B, p_2)

    print(p_1A)
    print(p_2B)

    q_1 = [0, -2, 8, 3]
    q_2 = [0, 0, 0]

    q_1A = evaluate_polynomial(A, q_1)
    q_2B = evaluate_polynomial(B, q_2)

    print(q_1A)
    print(q_2B)

    print(A.mult_tropical_matrix(B))
    print(B.mult_tropical_matrix(A))

    alice_public_term = p_1A.mult_tropical_matrix(p_2B)
    print(alice_public_term)

    bob_public_term = q_1A.mult_tropical_matrix(q_2B)
    print(bob_public_term)

    print(generate_key(bob_public_term, A, B, p_1, p_2))
    print(generate_key(alice_public_term, A, B, q_1, q_2))
