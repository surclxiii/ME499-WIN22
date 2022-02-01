import csv


# Problem 1
def load_data_from_file(path):
    # Takes a file path as a string, returns two lists
    filename = open(path)
    reader = csv.reader(filename)
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
def estimates_value(path):
    # Take time and position from load data function
    time, position = load_data_from_file(path)
    # Determine maximum, initial, final position
    c_max = max(position)
    c_initial = position[0]
    c_final = position[-1]
    return time, position, c_max, c_initial, c_final


# Problem 3
def estimate_char(path):
    # Take values from estimates_value to estimate characteristic
    time, position, c_max, c_initial, c_final = estimates_value(path)
    # Determine outputs
    p_ten = ((c_final - c_initial) * 0.1) + c_initial
    p_ninety = ((c_final - c_initial) * 0.9) + c_initial
    p_diff = p_ten - p_ninety
    p_ten_index = greater_than_index(position, p_ten)
    p_ninety_index = greater_than_index(position, p_ninety)
    time_ten = time[p_ten_index]
    time_ninety = time[p_ninety_index]
    # Rise time
    time_r = time_ninety - time_ten
    p_peak_index = greater_than_index(position, c_max)
    # Peak time
    time_p = time[p_peak_index]
    # Percentage overshoot
    percent_overshoot = (abs((c_max - c_final) / (c_initial - c_final)) * 100) - 100
    pos_ini_index = greater_than_index(position, (c_initial - p_diff) * 0.02)
    pos_final_index = greater_than_index(position, (c_final - p_diff) * 0.02)
    time_ini_two = time[pos_ini_index]
    time_final_two = time[pos_final_index]
    # Settling time
    time_s = abs(time_ini_two - time_final_two)
    mass = 1
    return time_r, time_p, percent_overshoot, time_s, mass


# PROBLEM 4
def get_system_params(percent_overshoot, time_s):
    # False declare to make the code rune
    s = 1
    w_n = 4/(s * time_s)
    spring_k = w_n ** 2
    damping_factor = w_n * 2 * s
    mass = 1
    return mass, spring_k, damping_factor


# Problem 5
def analyze_data(path):
    time, position, c_max, c_initial, c_final = estimates_value(path)
    time_r, time_p, percent_overshoot, time_s, mass = estimate_char(path)
    mass, spring_k, damping_factor = get_system_params(percent_overshoot, time_s)
    dict1 = {"c_initial": c_initial, "c_final": c_final, "c_max": c_max, "rise_time": time_r, "peak_time": time_p,
            "percent_overshoot": percent_overshoot, "settling_time": time_s, "system_mass": mass,
            "system_spring": spring_k, "system_damping": damping_factor}
    sort_dict = sorted(dict1.items())
    for i, j in sort_dict:
        print(i, j)


if __name__ == '__main__':
    path = 'data1.csv'
    print(analyze_data(path))
    # list = [1, 3, 4, 7, 10]
    # print(list)
    # print(greater_than_index(list, 6))
    # time, position, c_max, c_initial, c_final = estimates_value('data1.csv')
    # time_r, time_p, percent_overshoot, time_s, mass = estimate_char('data1.csv')
    # mass, spring_k, damping_factor = get_system_params(percent_overshoot, time_s)
    # print('c_initial:', c_initial)
    # print('c_max:', c_max)
    # print('c_final:', c_final)
    # print('timr_r:', time_r)
    # print('time_p:', time_p)
    # print('time_s:', time_s)
    # print('percent_overshoot:', percent_overshoot)
    # print('mass:', mass)
