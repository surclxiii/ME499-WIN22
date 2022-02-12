
import csv
import math


# Work with Ittiwat Poonprachasin
# Problem 1
def load_data_from_file(path):
    # Takes a file path as a string, returns two lists
    file = open(path, 'r')
    # Read only
    reader = csv.reader(file)
    header = next(reader)
    time = []
    position = []
    for row in reader:
        time.append(float(row[0]))
        position.append(float(row[1]))
    file.close()
    return time, position


def greater_than_index(l, n):
    for i in l:
        # Check if the element is greater than or equal to n
        if i >= n:
            # Return the index
            return l.index(i)
    return


# Problem 2
def estimates_value(path):
    # Take time and position from load data function
    time, position = load_data_from_file(path)
    # Determine initial, maximum, final position
    c_initial = position[0]
    c_max = max(position)
    c_final = position[-1]
    return time, position, c_initial, c_max, c_final


# Problem 3
def estimate_char(path):
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
    bounds = 0.02 * (abs(c_initial) + abs(c_final))
    upper = greater_than_index(position, (c_final + bounds))
    lower = greater_than_index(position, (c_final - bounds))
    time_up = time[upper]
    time_low = time[lower]
    # Settling time
    T_s = time_up - time_low
    return t_r, t_p, percent_overshoot, T_s


# PROBLEM 4
def get_system_params(percent_overshoot, T_s):
    zeta = (-math.log(percent_overshoot / 100)) / math.sqrt((math.pi ** 2) + (math.log(percent_overshoot / 100)) ** 2)
    w_n = 4 / (zeta * T_s)
    k = w_n ** 2
    c = w_n * 2 * zeta
    m = 1
    return k, c, m


# Problem 5
def analyze_data(path):
    time, position, c_initial, c_max, c_final = estimates_value(path)
    t_r, t_p, percent_overshoot, T_s = estimate_char(path)
    k, c, m = get_system_params(percent_overshoot, T_s)
    unsorted_dict = {'c_initial': c_initial, 'c_max': c_max, 'c_final': c_final, 'rise_time': t_r,
                     'peak_time': t_p, 'perc_overshoot': percent_overshoot, 'settling_time': T_s, 'system_mass': m,
                     'system_spring': k, 'system_damping': c}
    return unsorted_dict


if __name__ == '__main__':
    path = 'data1.csv'
    data = analyze_data(path)
    sorted_data = sorted(data.items())
    for key, value in sorted_data:
        print(key, value)