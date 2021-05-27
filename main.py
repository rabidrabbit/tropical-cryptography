from key_exchange_protocol import *

def pprint_matrix(matrix):
   print('\n'.join(['  '.join([str(cell) for cell in row]) for row in matrix.entries]))

if __name__ == "__main__":
   matrix_size = 2
   min_matrix_term = -10 ** 11
   max_matrix_term = 10 ** 11
   min_polynomial_coefficient = -10 ** 11
   max_polynomial_coefficient = 10 ** 11
   max_polynomial_degree = 10

   print("Generating polynomials...")

   print("Alice's two private polynomials are:")
   alice_polynomial_one = generate_random_tropical_poly(max_polynomial_degree, min_polynomial_coefficient, max_polynomial_coefficient)
   alice_polynomial_two = generate_random_tropical_poly(max_polynomial_degree, min_polynomial_coefficient, max_polynomial_coefficient)
   print(get_polynomial_representation(alice_polynomial_one))
   print(get_polynomial_representation(alice_polynomial_two))

   print("Bob's two private polynomials are:")
   bob_polynomial_one = generate_random_tropical_poly(max_polynomial_degree, min_polynomial_coefficient, max_polynomial_coefficient)
   bob_polynomial_two = generate_random_tropical_poly(max_polynomial_degree, min_polynomial_coefficient, max_polynomial_coefficient)
   print(get_polynomial_representation(bob_polynomial_one))
   print(get_polynomial_representation(bob_polynomial_two))

   print("Alice has the public matrix")
   alice_public_matrix = generate_random_matrix(matrix_size, min_matrix_term, max_matrix_term)
   pprint_matrix(alice_public_matrix)

   print("Bob has the public matrix")
   bob_public_matrix = generate_random_matrix(matrix_size, min_matrix_term, max_matrix_term)
   pprint_matrix(bob_public_matrix)

   print("Evaluating polynomials...")
   print("Alice sent Bob the following public term:")
   alice_p1_a = evaluate_polynomial(alice_public_matrix, alice_polynomial_one)
   alice_p2_b = evaluate_polynomial(bob_public_matrix, alice_polynomial_two)
   alice_msg = alice_p1_a.mult_tropical_matrix(alice_p2_b)
   pprint_matrix(alice_msg)

   print("Bob sent Alice the following public term:")
   bob_p1_a = evaluate_polynomial(alice_public_matrix, bob_polynomial_one)
   bob_p2_b = evaluate_polynomial(bob_public_matrix, bob_polynomial_two)
   bob_msg = bob_p1_a.mult_tropical_matrix(bob_p2_b)
   pprint_matrix(bob_msg)

   print("Alice and Bob are now calculating keys...")
   print("Alice generated the key:")
   alice_key = generate_key(bob_msg, alice_public_matrix, bob_public_matrix, alice_polynomial_one, alice_polynomial_two)
   pprint_matrix(alice_key)

   print("Bob generated the key:")
   bob_key = generate_key(alice_msg, alice_public_matrix, bob_public_matrix, bob_polynomial_one, bob_polynomial_two)
   pprint_matrix(bob_key)