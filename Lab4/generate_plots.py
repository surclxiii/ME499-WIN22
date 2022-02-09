import msd
import utils
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


if __name__ == '__main__':
    smd = msd.MassSpringDamper(m=1.0, k=5.0, c=2.5)
    state, t = smd.simulate(1.0, -1.0, 40, 0.01)
    plt.figure(1)
    plt.plot(t, state)
    plt.xlim([0, 10])
    plt.title("Spring Damper System")
    plt.xlabel("time (s)")
    plt.ylabel("Position (m)")
    plt.show()
    plt.clf()
    result = []
    for run_times in range(1000):
        result.append(utils.simulate_gachapon(15))
    plt.figure(2)
    n, bins, patches = plt.hist(result, 50, density=1, facecolor='g', alpha=0.75)
    plt.show()
    plt.clf()