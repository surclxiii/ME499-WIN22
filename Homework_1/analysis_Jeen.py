import csv
import math as np

"Problem 1"


def load_data_from_file(a):
    file = open(a)
    reader = csv.reader(file)
    header = next(reader)
    time = []
    position = []
    for row in reader:
        # print(row[0], row[1])
        time.append(float(row[0]))
        position.append(float(row[1]))
    file.close()
    return time, position


def greater_than_index(a, b):
    c = 0
    for number in a:
        if number < b:
            c = c + 1
        else:
            return c


# if __name__ == '__main__':
#      print(greater_than_index([1, 2, 3, 6, 7, 8], 5))

"Problem 2"


# time, position = load_data_from_file()

# def required_pos(a):
#     time, position =

# if __name__ == '__main__':
#      time, position = estimates_values()

def estimates_value(b):
    time, position = load_data_from_file(b)
    c_max = max(position)
    # c_max_time = max(time)
    c_initial = position[0]
    # c_initial_time = time[0]
    c_final = position[-1]
    # c_final_time = time[-1]

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

    overshoot_p = (abs((c_max - c_final) / (c_final - c_initial)) * 100)

    "two percent"
    # pos_ini_index = greater_than_index(position, (c_initial - p_diff) * 0.02)
    # pos_final_index = greater_than_index(position, (c_final - p_diff) * 0.02)
    boundaries = (abs(c_final) + abs(c_initial))*0.02
    up_bound = greater_than_index(position, (c_final + boundaries))
    low_bound = greater_than_index(position, (c_final - boundaries))
    get_time_up = time[up_bound]
    get_time_low = time[low_bound]
    get_time = get_time_up - get_time_low
    # time_final_two = time[pos_final_index]
    time_s = get_time

    mass = 1

    return time_r, time_p, overshoot_p, time_s, mass


def get_system_params(overshoot, settling_time):
    s = (-np.log(overshoot / 100)) / np.sqrt((np.pi ** 2) + (np.log(overshoot / 100)) ** 2)
    w_n = 4/(s * settling_time)
    spring_constant = w_n ** 2
    damping_factor = w_n * 2 * s
    mass = 1
    return mass, spring_constant, damping_factor


def analyze_data(filename):
    time, position, c_max, c_initial, c_final = estimates_value(filename)
    time_r, time_p, overshoot_p, time_s, mass = estimate_char(filename)
    mass, spring_constant, damping_factor = get_system_params(overshoot_p, time_s)
    dict1 = {"c_initial": c_initial, "c_final": c_final, "c_max": c_max, "rise_time": time_r, "peak_time": time_p,
             "perc_overshoot": overshoot_p, "settling_time": time_s, "system_mass": mass,
             "system_spring": spring_constant,
             "system_damping": damping_factor}
    sort_dict1 = sorted(dict1.items())
    for k, v in sort_dict1:
        print(k, v)


if __name__ == '__main__':
    # time, position, c_max, c_initial, c_final = estimates_value('data1.csv')
    # time_r, time_p, overshoot_p, time_s, mass = estimate_char('data1.csv')
    # # print(c_initial)
    # print(overshoot_p)
    # print(get_system_params(overshoot_p, time_s))
    analyze_data('data1.csv')

#
# def c_max_time(b):
#     time, position = load_data_from_file(b)
#     return max(time)
#
# def c_initial(b):
#     time, position = load_data_from_file(b)
#     return position[0]
#
# def c_initial_time(b):
#     time, position = load_data_from_file(b)
#     return time[0]
#
#
# def c_final(b):
#     time, position = load_data_from_file(b)
#     return position[-1]
#
#
# def c_final_time(d):
#     time, position = load_data_from_file(d)
#     return time[-1]
#


"Problem 3"

"finding the initial(10 percent)"
# def time_rise(e):
#     time, position = load_data_from_file(e)
#
#     p_ten = ((c_final(e) - c_initial(e))*0.1) + c_initial(e)
#     p_ninety = ((c_final(e) - c_initial(e))*0.9) + c_initial(e)
#     # p_diff = p_ten - p_ninety
#     p_ten_index = greater_than_index(position, p_ten)
#     p_ninety_index = greater_than_index(position, p_ninety)
#     time_ten = time[p_ten_index]
#     time_ninety = time[p_ninety_index]
#     t_r = time_ninety - time_ten
#     return t_r
#

#
# def
#
#
# if __name__ == '__main__':
#
#     print(c_max('data1.csv'))
#     print(c_initial_time('data1.csv'))
#     print(c_final('data1.csv'))
#     print(c_final_time('data1.csv'))
#     print(time_rise('data1.csv'))
#     print(load_data_from_file('data1.csv'))
#     print(time_rise('data1.csv'))
#     print(time_peak('data1.csv'))
