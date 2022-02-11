#!/usr/bin/env python

from scipy.integrate import odeint
from numpy import arange

class MassSpringDamper:
    """
    Simulated mass-spring-damper system, using the ode solver from scipy

    Usage:

    First, initialize a system with your desired mass, spring constant, and damper constants, like such:
    system = MassSpringDamper(2, 1, 0.5)

    Then, using this system, call simulate with your desired initial conditions (see the docstring for simulate()).
    Example:
    state, time = system.simulate(0.5, -0.5, 50)
    """

    def __init__(self, m, k, c):
        self.m = m
        self.k = k
        self.c = c

    def simulate(self, x, x_dot, t=100.0, dt=0.01):
        """
        Simulates a mass spring damper system using the given starting characteristics and time steps.
        :param x: Initial position (a float)
        :param x_dot: Initial velocity (a float)
        :param t: Time to simulate system (a positive float)
        :param dt: Time step used to approximate continuous solution of the ODE (a positive float)
        :return: A tuple of two elements.
            The first element is a Tx2 array with the system's position and velocity in each column.
            The second element is an array of length T with the corresponding times of the system.
        """

        initial_state = [x, x_dot]
        times = arange(0.0, t, dt)  # Set the simulation timesteps

        # Do the simulation
        state = odeint(lambda s,t: self.equation(s, t), initial_state, times)

        # Return the states (as [x, x_dot]) and the simulation timesteps
        return state,times
    
    # This function takes the current state [x, x_dot] and returns the
    # next velocity and acceleration [x_dot and x_dot_dot].  The
    # function is used by the scipy ode solver.
    def equation(self, state, t):
        # unpack the state vector
        x = state[0]
        x_dot = state[1]
        
        # compute acceleration xdd
        x_dot_dot = -self.k / self.m * x - self.c / self.m * x_dot

        return [x_dot, x_dot_dot]
  

if __name__ == '__main__':
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
    state,t = smd.simulate(0.0, 1.0)
