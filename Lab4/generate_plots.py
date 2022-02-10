import counter
import matplotlib.pyplot as plt
import msd
import time
import utils


if __name__ == '__main__':
    # Problem 1: Plot spring damper system
    smd = msd.MassSpringDamper(m=1.0, k=5.0, c=2.5)  # mass of 1.0, spring constant = 5.0, spring damper = 2.5
    state, t = smd.simulate(1.0, -1.0, 40, 0.01)  # start: 1.0, initial velocity: -1.0, time: 40sec, increment: 0.01
    plt.figure(1)
    plt.plot(t, state)  # Plot time vs position
    plt.xlim([0, 10])  # X-axes from 0 to 10
    plt.title("Spring Damper System")
    plt.xlabel("time (s)")
    plt.ylabel("Position (m)")
    plt.savefig('Problem1.png')
    plt.show()
    # Problem 2: Histogram of the gachapon problem
    result = []  # new result list
    for run_times in range(1000):  # Run simulation for 1000 times
        result.append(utils.simulate_gachapon(no_prize=15))  # Save result to the list
    plt.figure(2)
    plt.hist(result, 40)  # Plot histrogram with bin size: 40
    plt.xlim(left=0)  # X-axes starts from 0
    plt.title("Percent of Boxes of cereal to get 15 prizes (bins=40)")
    plt.xlabel("Boxes ")
    plt.ylabel("Percent")
    plt.savefig('Problem2.png')
    plt.show()
    # Problem 3: Algorithmic runtimes
    for value in range(50, 2550, 50):  # For all values 50, 100, ... up to 2500
        time_1 = time.time()  # Start counter
        list_random = utils.random_list(value)  # Get random list
        list_element_count = counter.get_element_counts(list_random)  # Count elements in random list
        time_2 = time.time()  # Stop counter
        delta_time = time_2 - time_1
        plt.scatter(value, delta_time)
    plt.title("List Lengths vs. Runtimes")
    plt.xlabel("List Lengths")
    plt.ylabel("Runtime (sec)")
    plt.savefig('Problem3.png')
    plt.show()
