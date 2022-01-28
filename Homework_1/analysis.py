import csv


def load_data_from_file(path):
    #  Takes a file path as a string, returns two lists
    data = open(path, 'r')
    file = csv.DictReader(data)
    time = []
    position = []
    for col in file:
        time.append(col['Time'])
        position.append(col['Position'])
    print('Time:', time)
    print('Position:', position)
load_data_from_file('data1.csv')

def greater_than_index(l, n):
    for i in l:
        # Check if the element is greater than or equal to n
        if i >= n:
            # Return the index
            return l.index(i)
    return


list = [1, 3, 4, 7, 10]
print(list)
print(greater_than_index(list, 6))
