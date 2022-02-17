import func
import sys
import numpy as np


class GachaponSimulator:
    """
    GachapnSimulator class with init of one argument
    Counting the iteration using class and calling function from utils
    """

    def __init__(self, prizes_n):
        self.prizes_n = prizes_n
        self.results = []

    def _simulate_once(self):
        counter = func.simulate_gachapon(self.prizes_n)
        return counter

    def reset(self):
        self.results.clear()
        return self.results

    def simulate(self, num_games):
        for times in range(num_games):
            self.results.append(func.simulate_gachapon(self.prizes_n))

        return self.results

    def get_summary_stats(self):
        n = len(self.results)
        if n > 1:
            mean_1 = sum(self.results) / len(self.results)

            stand = np.std(self.results)

            summary_dict = {'n': len(self.results),
                            'mean': mean_1,
                            'stdev': np.std(self.results)}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(mean_1),
                  "standard deviation of %s" % stand)

            return summary_dict

        elif n == 1:
            mean_one = sum(self.results) / len(self.results)
            stand = None
            summary_dict = {'n': len(self.results),
                            'mean': mean_one,
                            'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(mean_one), "standard deviation of %s" % stand)
            return summary_dict
        else:
            mean_else = None
            summary_dict = {'n': len(self.results),
                            'mean': mean_else,
                            'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(str(mean_else)), "standar deviation of {}".format(None))
            print(summary_dict)
            return summary_dict


if __name__ == '__main__':
    GS = GachaponSimulator(int(sys.argv[1]))
    GS.simulate(int(sys.argv[2]))
    GS._simulate_once()
    GS.get_summary_stats()