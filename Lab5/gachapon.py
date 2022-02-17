import numpy as np
import sys
import utils


class GachaponSimulator(object):
    def __init__(self, prizes_n):
        """
        Initializing parameter and attribute
        :param prizes_n: number of prizes
        """
        self.prizes_n = prizes_n
        self.results = []  # Empty list

    def _simulate_once(self):
        """
        Run one simulation
        :return: number of iterations took
        """
        num_iterations = utils.simulate_gachapon(self.prizes_n)  # Use function from lab 4
        return num_iterations

    def reset(self):
        """
        Reset attribute
        :return: Empty list
        """
        self.results = []  # Reset with empty list
        return self.results

    def simulate(self, num_games):
        """
        Run simulation for num_games times and record the number of iterations for each game.
        :param num_games: numbers of game to simulate
        :return: number of iterations for each game
        """
        for times in range(num_games):  # for how many games
            self.results.append(utils.simulate_gachapon(self.prizes_n))  # Record the number
        return self.results

    def get_summary_stats(self):
        """
        Get summary of the games
        :return: Dictionary with the number, mean, std_sum of games which have been currently been run
        """
        n = len(self.results)  # ongoing games
        std_sum = np.std(self.results)
        if n > 1:
            mean_sum = sum(self.results) / n
            dict_sum = {'n': n, 'mean': mean_sum, 'stdev': std_sum}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(n))
            print("Average number of iterations was {}".format(mean_sum), "standard deviation of %s" % std_sum)
            return dict_sum

        elif n == 1:
            mean_sum = sum(self.results) / n
            dict_sum = {'n': n, 'mean': mean_sum, 'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(n))
            print("Average number of iterations was {}".format(mean_sum), "standard deviation of %s" % std_sum)
            return dict_sum

        else:
            dict_sum = {'n': n, 'mean': None, 'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(n))
            print("Average number of iterations was {}".format(None), "standard deviation of {}".format(None))
            return dict_sum


if __name__ == "__main__":
    """
    CLI of the simulation
    :argument: (number of prizes, number of games to play)
    """
    our_sim = GachaponSimulator(int(sys.argv[1]))  # input number of prizes
    our_sim.simulate(int(sys.argv[2]))  # input number of games
    our_sim._simulate_once()
    our_sim.get_summary_stats()
