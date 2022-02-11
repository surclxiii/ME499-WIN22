import random


# Problem 2: Histogram of the gachapon problem
def sanity_check(prize_pool, no_prize):
    """
    Check if simulate_gachapon() returns a valid number
    :param prize_pool: list of the prizes in pool
    :param no_prize: number of the prize(s)
    :return: Boolean, True if the prize is included in prize pool, False if the prize is not included in prize pool
    """
    if len(prize_pool) < no_prize:  # False: Not all prizes yet, if number of prize pool < number of prizes
        return False  # You can't get n prize(s) with n-1 attempts
    else:
        for prize in range(no_prize):  # Iteration upto the range of n (number of prizes - 1)
            if prize not in prize_pool:  # False: If prize is not included
                return False
        return True  # True: if prize is included in n (number of prizes - 1)


def simulate_gachapon(no_prize):
    """
    Simulate the gachapon buying and get the number of attempts
    :param no_prize: number of prizes in the prize pool
    :return: number of attempts
    """
    prize_pool = []  # list for prize pool
    no_iteration = 0  # attempts counter
    while not sanity_check(prize_pool, no_prize):  # Check if prize pool have recieved all prizes(no_prize)
        prize_pool.append(random.randrange(0, no_prize))  # Random new number
        no_iteration += 1   # Attempts
    return no_iteration


def random_list(length):
    """
    Get a random list
    :param length: length of random list
    :return: list of random values
    """
    list_random = []
    for element in range(0, length):
        list_random.append(random.randint(0, length - 1))
    return list_random
