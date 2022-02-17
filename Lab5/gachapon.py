import func
import numpy as np
import sys


class GachaponSimulator(object):
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
            mean_less = sum(self.results) / len(self.results)
            std = np.std(self.results)
            dict_sum = {'n': len(self.results), 'mean': mean_less,
                        'stdev': std}
            print("Running {} prizes".format(self.prizes_n), "Lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(mean_less),
                  "standard deviation of %s" % std)
            return dict_sum

        elif n == 1:
            mean_isone = sum(self.results) / len(self.results)
            std = None
            dict_sum = {'n': len(self.results),
                            'mean': mean_isone,
                            'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(mean_isone), "standard deviation of %s" % std)
            return dict_sum

        else:
            mean_else = None
            dict_sum = {'n': len(self.results),
                            'mean': mean_else,
                            'stdev': None}
            print("Running {} prizes".format(self.prizes_n), "lottery simulator {} times".format(len(self.results)))
            print("Average number of iterations was {}".format(str(mean_else)), "standard deviation of {}".format(None))
            print(dict_sum)
            return dict_sum


if __name__ == "__main__":
    our_sim = GachaponSimulator(int(sys.argv[1]))
    our_sim.simulate(int(sys.argv[2]))
    our_sim._simulate_once()
    our_sim.get_summary_stats()