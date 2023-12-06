#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in row] for row in matrix]
    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            new_matrix[row][elem] = matrix[row][elem] ** 2
    return new_matrix
