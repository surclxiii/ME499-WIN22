import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import optimize


def eggholder(x, y):
    """
    Takes in either a scalar x and y, or a 1-D numpy array for both x and y.
    """
    if (isinstance(x, np.ndarray) and not isinstance(y, np.ndarray)) or (
            isinstance(y, np.ndarray) and not isinstance(x, np.ndarray)):
        pass

    result = -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))
    if isinstance(x, np.ndarray):
        outside = (np.abs(x) > 512) | (np.abs(y) > 512)
        result[outside] = 2000
        return result
    else:
        return 2000 if (abs(x) > 512 or abs(y) > 512) else result


def minimize_eggholder(guess, max_calls=100):
    """
    Find minimum of eggholder function
    :param guess: Initial guess
    :param max_calls: Maximum number of function evaluations to make.
    :return: The (x,y) coordinate which minimizes the function, followed by the actual value at the minimum.
    """
    func = lambda egg: eggholder(egg[0], egg[1])
    minimum = optimize.fmin(func, guess, maxfun=max_calls, full_output=True, disp=False)
    return minimum[0], minimum[1]


if __name__ == '__main__':
    "Randomly generates 1000 points"
    x = random.randrange(-512, 512, 1000)
    y = random.randrange(-512, 512, 1000)
    co_xy = []
    results = minimize_eggholder([x, y])
    subtract_dist = abs(404.123 - results[1])
    "Absolute difference"
    for index in range(len(results[0])):
        subtract_co = abs(512 - results[0][index])
        co_xy.append(subtract_co)
    values = (co_xy, subtract_dist)
    "Plotting"
    plt.hist(values, bins=25)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Eggholder')
    plt.show()
