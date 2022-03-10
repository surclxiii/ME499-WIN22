import numpy as np


def compute_inertia_matrix(matrix, mass=1):
    """
    Compute inertia matrix
    :param matrix: Nx3 array of a matrix
    :param mass: optional
    :return: 3x3 Numpy array representing the inertia matrix
    """
    n = np.array(matrix)
    m_i = mass / int((np.size(n) / 3))
    x_i = matrix[:, 0]
    y_i = matrix[:, 1]
    z_i = matrix[:, 2]
    sum_i = np.array([[np.sum(m_i * (y_i ** 2 + z_i ** 2)), np.sum(-m_i * (x_i * y_i)), np.sum(-m_i * (x_i * z_i))],
                      [np.sum(-m_i * (x_i * y_i)), np.sum(m_i * (x_i ** 2 + z_i ** 2)), np.sum(-m_i * (y_i * z_i))],
                      [np.sum(-m_i * (x_i * z_i)), np.sum(-m_i * (y_i * z_i)), np.sum(m_i * (x_i ** 2 + y_i ** 2))]])
    return sum_i


def sample_sphere_polar(n):
    """
    Generate random points on a sphere surface with angle-azimuth
    :param n: N single value
    :return: nx3 Numpy array with sphere points sampled
    """
    azi_points = []
    r = 1
    phi = np.random.uniform(0, np.pi, size=n)
    theta = np.random.uniform(0, 2 * np.pi, size=n)
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    azi_points = np.column_stack([x, y, z])
    return azi_points


def sample_sphere_gaussian(n):
    """
    Generate random points on a sphere surface with Gaussian distribution
    :param n: N single value
    :return: nx3 Numpy array with sphere points sampled
    """
    gaus_points = []
    sample = np.random.normal(size=(n, 3), loc=0, scale=1)
    magnitude = np.sum(np.abs(sample) ** 2, axis=1) ** (1/2)
    gaus_points = sample.transpose() / magnitude.transpose()
    return gaus_points.transpose()


def test_inertia_matrices_output():
    """
    Test intertia matrices output
    :return: inertia matrices
    """
    m = 1
    r = 1
    n = 1000
    gaus = compute_inertia_matrix(sample_sphere_gaussian(n))
    polar = compute_inertia_matrix(sample_sphere_polar(n))
    ixx = iyy = izz = (2.0 / 3.0) * r ** 2 * m
    ixy = 0.0
    ixz = 0.0
    iyz = 0.0
    expected = np.column_stack([[ixx, ixy, ixz], [ixy, iyy, iyz], [ixz, iyz, izz]])
    np.set_printoptions(precision=3, suppress=True)
    return print("Polar:\n", polar, "\nGaussian:\n", gaus, "\nExpected:\n", expected)
