import csv
import math as np


# Problem 1

def load_data_from_file(path):
    #  Takes a file path as a string, returns two lists
    filename = open(path, 'r')
    reader = csv.reader(path)
    header = next(reader)
    time = []
    position = []
    for row in reader:
        time.append(float(row[0]))
        position.append(float(row[1]))
    filename.close()
    return time, position


def greater_than_index(l, n):
    for i in l:
        # Check if the element is greater than or equal to n
        if i >= n:
            # Return the index
            return l.index(i)
    return


# Problem 2
def estimates_value(b):
    time, position = load_data_from_file(b)
    c_max = max(position)
    c_initial = position[0]
    c_final = position[-1]
    return time, position, c_max, c_initial, c_final


def estimate_char(a):
    time, position, c_max, c_initial, c_final = estimates_value(a)

    p_ten = ((c_final - c_initial) * 0.1) + c_initial
    p_ninety = ((c_final - c_initial) * 0.9) + c_initial
    p_diff = p_ten - p_ninety
    p_ten_index = greater_than_index(position, p_ten)
    p_ninety_index = greater_than_index(position, p_ninety)
    time_ten = time[p_ten_index]
    time_ninety = time[p_ninety_index]
    time_r = time_ninety - time_ten

    p_peak_index = greater_than_index(position, c_max)
    time_p = time[p_peak_index]

    overshoot_p = (abs((c_max - c_final) / (c_initial - c_final)) * 100) - 100

    "two percent"
    pos_ini_index = greater_than_index(position, (c_initial - p_diff) * 0.02)
    pos_final_index = greater_than_index(position, (c_final - p_diff) * 0.02)
    time_ini_two = time[pos_ini_index]
    time_final_two = time[pos_final_index]
    time_s = abs(time_ini_two - time_final_two)

    mass = 1

    return time_r, time_p, overshoot_p, time_s, mass

def get_system_params(overshoot, settling_time):
    s = (-np.log(overshoot / 100)) / np.sqrt((np.pi ** 2) + (np.log(overshoot / 100)) ** 2)
    w_n = 4/(s * settling_time)
    spring_constant = w_n ** 2
    damping_factor = w_n * 2 * s
    mass = 1
    return mass, spring_constant, damping_factor

def analyze_data(path):
    time, position, c_max, c_initial, c_final = estimates_value(path)
    time_r, time_p, overshoot_p, time_s, mass = estimate_char(path)
    mass, spring_constant, damping_factor = get_system_params(overshoot_p, time_s)
    dict1 = {"c_initial": c_initial, "c_final": c_final, "c_max": c_max, "rise_time": time_r, "peak_time": time_p,
             "perc_overshoot": overshoot_p, "settling_time": time_s, "system_mass": mass,
             "system_spring": spring_constant,
             "system_damping": damping_factor}
    sort_dict1 = sorted(dict1.items())
    for k, v in sort_dict1:
        print(k, v)

if __name__ == '__main__':
    estimates_value('data1.csv')