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
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # x-axis
    faces_sum = roll.sum(axis=1)
    plt.hist(faces_sum, faces)
    plt.show()
    file_name = 'dice_{0}_rolls_{1}.png'.format(num_rolls, iterations)
    plt.savefig(file_name)
    plt.close()
    return faces_sum


def nearest_neighbors(a, b, c):
    if np.sum(np.square(a-b)) < c:
        return a
    
    nn_func = np.vectorize(nearest_neighbors)
    result = nn_func(a, b, c)
    result = result[~np.isnan(result).any(axis=1)]
    result = sorted(result, key=lambda result:result[0])
    result = sorted(result, key=lambda result:result[1])
    result = sorted(result, key=lambda result:result[2])


if __name__ == '__main__':
    simulate_dice_rolls(1, 100)
    array = np.array([[1, 1, 1], [2, 3, 5], [0, 1, 1], [1.5, 1, 1], [10, 9, 9]])
    target_pt = np.array([0, 1, 1])
    nearest_neighbors(array, target_pt, 3)