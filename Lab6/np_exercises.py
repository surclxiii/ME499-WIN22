from matplotlib import pyplot as plt
import numpy as np


def numpy_close(a, b, tol=1e-8):
    """
    Check if the shape of array is identical (optional: within tolerance)
    :param a: array a
    :param b: array b
    :param tol: tolerance
    :return: True/False
    """
    array_a = np.array(a)  # make a into array if not yet
    array_b = np.array(b)
    if array_a.shape == array_b.shape and np.all(abs(array_a - array_b) < tol):
        return True
    else:
        return False


def simple_minimizer(func, start, end, num=100):
    """
    Get minimum f(x) and the x corresponding to the minimum
    :param func: 1D function
    :param start: int start point
    :param end: int end point
    :param num: int evenly space
    :return: (x at minimum f(x) and minimum f(x))
    """
    if start > end:
        raise ValueError('End value has to greater than Start value')
    else:
        x = np.linspace(start, end, num)  # Evenly space
        y = func(x)
        y_min = np.min(y)  # Find min
        y_min_i = np.where(y == y_min)  # Find index
        y_min_i = y_min_i[0][0]
        x_ymin = x[y_min_i]  # Get the value at that index
    return x_ymin, y_min


def simulate_dice_rolls(num_rolls, iterations):
    """
    Dice Roll Simulator
    :param num_rolls: int number want to observe
    :param iterations: int how many times
    :return: 1-D Numpy array of length iterations, where each item is the sum of throwing a fair 6-sided die
num_rolls times.
    """
    roll = np.random.randint(1, 7, size=(iterations, num_rolls))
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # x-axis
    faces_sum = roll.sum(axis=1)
    plt.hist(faces_sum, faces)
    plt.show()
    file_name = 'dice_{0}_rolls_{1}.png'.format(num_rolls, iterations)
    plt.savefig(file_name)
    plt.close()
    return faces_sum


def is_transformation_matrix(matrix_array):
    """
    Check if the transformation matrix is valid
    :param matrix_array: array of 4x4
    :return: True/False if transformation matrix is valid
    """
    matrix = np.array(matrix_array[0:3, 0:3])  # Creat a matrix
    bottom = np.array([0., 0., 0., 1.])  # Set the bottom row
    matrix_iden = np.identity(3)  # Create identity matrix
    matrix_trans = np.transpose(matrix)  # Transposing
    if np.all(np.matmul(matrix_trans, matrix) - matrix_iden < 1e-5) and np.all(matrix_array[3] == bottom):
        return True
    else:
        return False


def nearest_neighbors(a, b, c):
    """
    Sort the output by distance from the corresponding point
    :param a: N x D Numpy array
    :param b: 1D array of length D point
    :param c: distance
    :return: Sorted output
    """
    def euclid_func(r):
        return np.linalg.norm(r - b)
    distance = np.apply_along_axis(euclid_func, 1, a)
    near_1 = a[np.where(distance < c)]
    near_2 = np.apply_along_axis(euclid_func, 1, near_1)
    sorted_out = near_1[np.argsort(near_2)]
    return sorted_out


# Work with Ittiwat, Maila, Breden
if __name__ == '__main__':
    simulate_dice_rolls(5, 2000)
