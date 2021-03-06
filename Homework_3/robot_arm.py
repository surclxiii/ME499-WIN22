import matplotlib.pyplot as plt
import numpy as np
from itertools import product

class RobotArm:

    def __init__(self, *arm_lengths, obstacles=None):
        """
        Represents an N-link arm with the arm lengths given.
        Example of initializing a 3-link robot with a single obstacle:

        my_arm = RobotArm(0.58, 0.14, 0.43, obstacles=[VerticalWall(0.45)])

        :param arm_lengths: Float values representing arm lengths of the robot.
        :param obstacles:
        """
        self.arm_lengths = np.array(arm_lengths)
        if np.any(self.arm_lengths < 0):
            raise ValueError("Cannot have negative arm length!")
        self.obstacles = []
        if obstacles is not None:
            self.obstacles = obstacles

    def __repr__(self):
        msg = '<RobotArm with {} links\nArm lengths: '.format(len(self.arm_lengths))
        msg += ', '.join(['{:.2f}'.format(length) for length in self.arm_lengths])
        msg += '\nObstacles: '
        if not len(self.obstacles):
            msg += 'None'
        else:
            msg += '\n\t' + '\n\t'.join(str(obstacle) for obstacle in self.obstacles)
        msg += '\n>'
        return msg

    def __str__(self):
        return self.__repr__()

    def get_links(self, thetas):
        """
        Returns all of the link locations of the robot as Link objects.
        :param thetas: A list or array of scalars matching the number of arms.
        :return: A list of Link objects.
        """

        cum_theta = np.cumsum(thetas)

        results = np.zeros((self.arm_lengths.shape[0] + 1, 2))

        results[1:, 0] = np.cumsum(self.arm_lengths * np.cos(cum_theta))
        results[1:, 1] = np.cumsum(self.arm_lengths * np.sin(cum_theta))
        links = [Link(start, end) for start, end in zip(results[:-1], results[1:])]

        return links

    def get_ee_location(self, thetas):
        """
        Returns the location of the end effector as a length 2 Numpy array.
        :param thetas: A list or array of scalars matching the number of arms.
        :return: A length 2 Numpy array of the x,y coordinate.
        """
        return self.get_links(thetas)[-1].end

    def ik_grid_search(self, target, intervals):
        start_int = np.linspace(0, 2*np.pi, num=intervals, endpoint=False)
        good_hits = np.array(list(product(start_int, repeat=len(self.arm_lengths))))
        my_goodlinks = []
        for i in range(len(good_hits)):
            if self.get_ee_location(good_hits[i]) is target:
                my_goodlinks.append(self.get_links(good_hits[i]))
        return my_goodlinks

    def ik_fmin_search(self, target, thetas_guess, max_calls=100):
        raise NotImplementedError

    def get_collision_score(self, thetas):
        """
        Calculate the collision score
        :param thetas: theta in rad
        :return: number of colission score
        """
        col_link = self.get_links(thetas)
        col_score = 0
        print(col_link)
        for all_links in col_link:
            for obstacles in self.obstacles:
                if all_links.check_wall_collision(obstacles):
                    col_score -= 1
        print("collision_score", col_score)
        return col_score

    def ik_constrained_search(self, target, thetas_guess, max_iters=100):
        raise NotImplementedError

    def plot_robot_state(self, thetas, target=None, filename='robot_arm_state.png'):
        """
        Plot the robot arm (work with Ittiwat)
        :param thetas: theta in rad
        :param target: (x,y) target point in the environment
        :param filename: file name
        :return:
        """
        link_arms = self.get_links(thetas)
        values = []
        if self.obstacles is not None:
            for obs in self.obstacles:
                plt.axvline(obs.loc)
                for lists in range(len(link_arms)):
                    values.append(link_arms[lists])
                    xs = link_arms[lists].start[0], link_arms[lists].end[0]
                    ys = link_arms[lists].start[1], link_arms[lists].end[1]
                    plt.plot(link_arms[lists].end[0], link_arms[lists].end[1], 'bo')
                    if values[lists].check_wall_collision(obs) is True:
                        plt.plot(xs, ys, '--', color='r')
                    else:
                        print(values[lists].check_wall_collision(obs))
                        plt.plot(xs, ys, color='k')
        if target is not None:
            plt.plot(target[0], target[1], 'bo', color='r')
        plt.savefig(filename)
        plt.show()
        plt.close()
        return


class Link:

    def __init__(self, start, end):
        """
        Represents a finite line segment in the XY plane, with start and ends given as 2-vectors
        :param start: A length 2 Numpy array
        :param end: A length 2 Numpy array
        """
        self.start = start
        self.end = end

    def __repr__(self):
        return '<Link: ({:.3f}, {:.3f}) to ({:.3f}, {:.3f})>'.format(self.start[0], self.start[1],
                                                                     self.end[0], self.end[1])

    def __str__(self):
        return self.__repr__()

    def check_wall_collision(self, wall):
        """
        Check if collision happen
        :param wall: x location of wall
        :return: True/False True if collide, False if not
        """
        if not isinstance(wall, VerticalWall):
            raise ValueError('Please input a valid Wall object to check for collision.')
        return self.start[0] < wall.loc < self.end[0] or self.start[0] > wall.loc > self.end[0]


class VerticalWall:

    def __init__(self, loc):
        """
        A VerticalWall represents a vertical line in space in the XY plane, of the form x = loc.
        :param loc: A scalar value
        """
        self.loc = loc

    def __repr__(self):
        return '<VerticalWall at x={:.3f}>'.format(self.loc)


if __name__ == '__main__':
    # Check Wall collision
    my_link = Link((1.1, 5.0), (3.0, 3.3))
    print('my_link:', my_link)
    print(my_link.check_wall_collision(VerticalWall(2.1)))
    print(my_link.check_wall_collision(VerticalWall(-0.3)))
    # Example of initializing a 3-link robot arm
    arm = RobotArm(1, 1, 1, obstacles=[VerticalWall(1.5)])
    print(arm)
    arm.get_collision_score([np.pi/2, 0, 0])
    arm.get_collision_score([0, 0, np.pi])
    # Ploting
    my_arm = RobotArm(2, 1, 2, obstacles=[VerticalWall(3.2)])
    my_arm.plot_robot_state([0.2, 0.4, 0.6], target=[1.5, 1.5])

    # Get the end-effector position of the arm for a given configuration
    thetas = [np.pi / 4, np.pi / 2, -np.pi / 4]
    pos = arm.get_ee_location(thetas)
    print('End effector is at: ({:.3f}, {:.3f})'.format(*pos))

    # Get each of the links for the robot arm, and print their start and end points
    links = arm.get_links(thetas)

    for i, link in enumerate(links):
        print('Link {}:'.format(i))
        print('\tStart: ({:.3f}, {:.3f})'.format(*link.start))
        print('\tEnd: ({:.3f}, {:.3f})'.format(*link.end))
