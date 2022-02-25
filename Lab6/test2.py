import numpy as np


def numpy_close(a, b, tol=1e-8):
    arr_a = np.array(a)
    arr_b = np.array(b)
    if arr_a.shape == arr_b.shape:
        return np.all(abs(arr_a - arr_b) < tol)
    else:
        return False


def simple_minimizer(func, start, end, num=100):
    if start > end:
        raise ValueError('Wrong input')
    x = np.linspace(start, end, num)
    y = func(x)
    min_y = np.amin(y)
    index_y_min = np.where(y == min_y)
    get_value = index_y_min[0][0]
    x_at_y = x[get_value]
    print(min_y)
    print(index_y_min)
    print(get_value)
    print(x_at_y)
    return x_at_y, min_y

if __name__ == '__main__':
    # print(numpy_close([1,2,3], [1,2,3,]))
    #
    # my_func = lambda x: x ** 2
    # print(simple_minimizer(my_func, -1.75, 2.25, num=5))

    # print(simulate_dice_rolls(1, 100))
    # tf_valid = np.array([[0, 0, -1, 4], [0, 1, 0, 2.4], [1, 0, 0, 3], [0, 0, 0, 1]])
    # tf_invalid = np.array([[1, 2, 3, 1], [0, 1, -3, 4], [0, 1, 1, 1], [-0.5, 4, 0, 2]])
    # print(is_transformation_matrix(tf_valid))  # True
    # print(is_transformation_matrix(tf_invalid))  # False
    my_func = lambda x: x ** 2
    print(simple_minimizer(my_func, 0, 10))