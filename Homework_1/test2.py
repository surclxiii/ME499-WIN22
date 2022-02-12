import csv
import math


# Work with Ittiwat Poonprachasin
# Problem 1
def load_data_from_file(path):
    """
    Takes a file path as a string, returns two lists
    :param path: file path
    :return: list of all time index, list of all the position values as floats
    """
    file = open(path, 'r')  # Read only
    reader = csv.reader(file)
    header = next(reader)
    time = []
    position = []
    for row in reader:  # Add datas from file to the lists
        time.append(float(row[0]))
        position.append(float(row[1]))
    file.close()
    return time, position


def greater_than_index(list, number):
    """
    Get the position of the first element in the list which is greater or equal to given number.
    :param list: A list of number
    :param number: single number
    :return: The index of the element
    """
    for index in list:
        # Check if the element is greater than or equal to n
        if index >= number:
            # Return the index
            return list.index(index)
    return


# Problem 2
def estimates_value(path):
    """
    Get the initial, largest, and final position of the system
    :param path: The file path
    :return: values of time, position, initial_pos, max_pos, final_pos
    """
    time, position = load_data_from_file(path)    # Take time and position from load data function
    # Determine initial, maximum, final position
    c_initial = position[0]
    c_max = max(position)
    c_final = position[-1]
    return time, position, c_initial, c_max, c_final


# Problem 3
def estimate_char(path):
    """
    Compute the characteristic of data from file
    :param path: file path
    :return: values of rising time, peak time, percent overshoot, settling time
    """
    # Take values from estimates_value to estimate characteristic
    time, position, c_initial, c_max, c_final = estimates_value(path)
    # 10% time
    p_ten = ((c_final - c_initial) * 0.1) + c_initial
    p_ten_i = greater_than_index(position, p_ten)
    time_ten = time[p_ten_i]
    # 90% time
    p_ninety = ((c_final - c_initial) * 0.9) + c_initial
    p_ninety_i = greater_than_index(position, p_ninety)
    time_ninety = time[p_ninety_i]
    # Rise time
    t_r = time_ninety - time_ten
    p_peak_i = greater_than_index(position, c_max)
    # Peak time
    t_p = time[p_peak_i]
    # Percentage overshoot
    percent_overshoot = (abs((c_max - c_final) / (c_final - c_initial)) * 100)
    # 2% time
    p_diff = p_ten - p_ninety
    pos_ini_index = greater_than_index(position, (c_initial - p_diff) * 0.02)
    pos_fin_index = greater_than_index(position, (c_final - p_diff) * 0.02)
    time_ini_two = time[pos_ini_index]
    time_final_two = time[pos_fin_index]
    # Settling time
    T_s = abs(time_ini_two - time_final_two)
    return t_r, t_p, percent_overshoot, T_s


# PROBLEM 4
def get_system_params(percent_overshoot, settling_time):
    """
    Get the system parameter (damping, mass, constant)
    :param percent_overshoot: percentage overshoot
    :param settling_time: settling time
    :return: values of system damping, system mass, system spring
    """
    zeta = (-math.log(percent_overshoot / 100)) / math.sqrt((math.pi ** 2) + (math.log(percent_overshoot / 100)) ** 2)
    w_n = 4 / (zeta * settling_time)
    k = w_n ** 2
    c = w_n * 2 * zeta
    m = 1
    return k, c, m


# Problem 5
def analyze_data(path):
    """
    Take in file name and get the dictionary with following keys, values
    :param path: file path
    :return: dictionary of keys, values
    """
    time, position, c_initial, c_max, c_final = estimates_value(path)
    t_r, t_p, percent_overshoot, T_s = estimate_char(path)
    k, c, m = get_system_params(percent_overshoot, T_s)
    unsorted_dict = {'c_initial': c_initial, 'c_max': c_max, 'c_final': c_final, 'rise_time': t_r,
                     'peak_time': t_p, 'perc_overshoot': percent_overshoot, 'settling_time': T_s, 'system_mass': m,
                     'system_spring': k, 'system_damping': c}
    return unsorted_dict


if __name__ == '__main__':
    path = 'Homework_1/data1.csv'
    data = analyze_data(path)
    sorted_data = sorted(data.items())
    for key, value in sorted_data:
        print(key, value)