import numpy as np

# Coding for one piece - % 4 (x) to get one axis and // 4 (y) to get the other
#
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15

I_shape = np.array([[1, 5, 9, 13],
                    [4, 5, 6, 7]])

O_shape = np.array([[5, 6, 9, 10]])

T_shape = np.array([[1, 4, 5, 6],
                    [1, 4, 5, 9],
                    [4, 5, 6, 9],
                    [1, 5, 6, 9]])

S_shape = np.array([[5, 6, 8, 9],
                    [1, 5, 6, 10]])

Z_shape = np.array([[5, 6, 10, 11],
                    [2, 5, 6, 9]])

L_shape = np.array([[4, 8, 9, 10],
                    [2, 6, 9, 10],
                    [4, 5, 6, 10],
                    [1, 2, 5, 9]])

shapes = (I_shape, O_shape, T_shape, S_shape, Z_shape, L_shape)
