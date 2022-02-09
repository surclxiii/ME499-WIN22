import random, math
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


def checkAll_prizes(prize_pool, no_prize):
    if len(prize_pool) < no_prize:  # False: Not all prizes yet, if number of prize pool < number of prizes
        return False    # You can't get n prize(s) with n-1 attempts
    else:
        for prize in range(no_prize):    # Iteration upto the range of n (number of prizes - 1)
            if prize not in prize_pool:  # False: If prize is not included
                return False
        return True     # True: if prize is included in n (number of prizes - 1)


def simulate_gachapon(no_prize):
    """"
    Should never return a number less than n.
    """
    prize_pool = []
    no_iteration = 0
    while not checkAll_prizes(prize_pool, no_prize):    # Check if have recieved all prizes
        # print(len(prize_pool), no_prize)
        prize_pool.append(math.floor(random.uniform(0, no_prize)))  # Random new number
        no_iteration += 1   # Counter
        # print(("prize_pool:", prize_pool, "no_iteration:", no_iteration))
    return no_iteration
