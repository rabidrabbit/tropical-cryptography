import math

class TropicalMatrix:
    def __init__(self, entries):
        self.entries = entries

    def __str__(self):
        return str(self.entries)

    def add_tropical_matrix(self, matrix):
        n = len(self.entries)
        new_matrix = self.get_empty_matrix(n, math.inf)
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = min(self.get_entry(i, j), matrix.get_entry(i, j))
        return TropicalMatrix(new_matrix)

    def mult_scalar(self, scalar):
        if type(scalar) is not int:
            print("Type not supported. Exiting")
            raise TypeError
        n = len(self.entries)
        new_matrix = self.get_empty_matrix(n)
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = self.get_entry(i, j) + scalar
        return TropicalMatrix(new_matrix)

    def mult_tropical_matrix(self, matrix):
        """
        Standard O(n^3) matrix multiplication except with tropical operations.
        """
        if type(matrix) is not TropicalMatrix:
            print("Type not supported. Exiting")
            raise TypeError

        n = len(self.entries)
        new_matrix = self.get_empty_matrix(n)
        for i in range(n):
            for j in range(n):
                sum_list = []
                for k in range(n):
                    sum_list.append(self.get_entry(i, k) + matrix.get_entry(k, j))
                new_matrix[i][j] = min(sum_list)
        return TropicalMatrix(new_matrix)

    def power(self, n):
        if n == 1:
            return self
        elif n < 1:
            raise ValueError("Invalid power.")

        cur_matrix = self
        new_matrix = None
        for i in range(n - 1):
            new_matrix = cur_matrix.mult_tropical_matrix(self)
            cur_matrix = new_matrix
        return new_matrix
    
    def get_entry(self, i, j):
        return self.entries[i][j]
    
    def get_dimension(self):
        return len(self.entries)
    
    def get_empty_matrix(self, n, val=None):
        return [[None] * n for i in range(n)]

if __name__ == "__main__":
    A = TropicalMatrix([[3, 2], [1, -2]])
    B = TropicalMatrix([[5, 7], [-3, -5]])
    C = A.power(2)
    print(C)