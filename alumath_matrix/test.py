from alumath_matrix.matrix_ops import Matrix

# Test 1: Simple 2x2 multiplication
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
C = A @ B
print("Test 1 (2x2 matrices):", C)  # Should print [[19, 22], [43, 50]]

# Test 2: Different dimensions (2x3 * 3x2)
D = Matrix([[1, 2, 3], [4, 5, 6]])  # 2x3
E = Matrix([[7, 8], [9, 10], [11, 12]])  # 3x2
F = D @ E
print("Test 2 (2x3 * 3x2):", F)  # Should print [[58, 64], [139, 154]]