import numpy as np
import math
def determinant(arr):
    #your code here
    matrix = np.array(arr)
    return round(np.linalg.det(matrix))