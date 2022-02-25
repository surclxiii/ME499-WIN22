"""
Work with Ittiwat
"""
import datetime
import fnmatch
import json
import matplotlib.pyplot as plt
import os
import requests


def get_current_day(unix_timestamp=None):
    """
    Get the current date from second since epoch. If non argument pass, return the current date.
    :param unix_timestamp: an integer Unix timestamp (the number of seconds since epoch)
    :return: string of corresponding day in UTC time (YYYY-MM-DD)
    """
    if unix_timestamp is None:  # Get today date
        current_day = datetime.date.today()

    else:  # Get date from the second since epoch
        current_day = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d')

    current_day = str(current_day)  # Convert to string
    return current_day


def query_carbon(date_iso=get_current_day(), use_cache=True):
    """
    Get the carbon data of the specific date
    :param date_iso: string of date in UTC time (YYYY-MM-DD)
    :param use_cache: choose if use data from cache or not
    :return: dictionary of carbon data for the given date
    """
    file_name = 'carbon_{}.json'.format(date_iso)  # Declare file name
    if os.path.isdir("data") is False:  # Check if the directory exist, if not create one
        os.mkdir('data')

    for file in os.listdir('data'):  # Check if the file already exist
        if fnmatch.fnmatch(file, file_name) is False:
            file_exists = False
        else:
            file_exists = True
            break

    if use_cache and file_exists is True:  # If the file exist, use cache
        file = open(os.path.join('data', 'carbon_{}.json'.format(date_iso)))
        cache = json.load(file)
        file.close()
        return cache

    else:  # If the cache is not exist, get data from web api
        headers = {'Accept': 'application/json'}
        web_api = 'https://api.carbonintensity.org.uk/intensity/date/{}'.format(date_iso)
        web_data = requests.get(web_api, params={}, headers=headers)
        if web_data.status_code == 400:  # Check status code
            raise Exception("Bad Request")
        elif web_data.status_code == 500:
            raise Exception("Internal Server Error")
        else:
            print('Status Code: ' + str(web_data.status_code))
            data_new = dict(web_data.json())
            with open(os.path.join('data', 'carbon_{}.json'.format(date_iso)), 'w') as outfile:  # Write to file
                json.dump(data_new, outfile, indent=4)
            print(data_new)
        return data_new


def plot_carbon(date_iso=get_current_day()):
    """
    Plot the carbon data of the specific date (Time (h) vs Intensity)
    :param date_iso: string of date in UTC time (YYYY-MM-DD)
    :return: Plot of the carbon
    """
    if os.path.isdir("plots") is False:  # Check if the directory exist, then create
        os.mkdir("plots")

    else:
        carbon_data = query_carbon(date_iso)  # Get data from function
        carbon_predicted = []
        carbon_realized = []
        for item in carbon_data['data']:
            carbon_predicted.append(item['intensity']['forecast'])
            carbon_realized.append(item['intensity']['actual'])
        time_step = [step * 0.5 for step in range(0, 48)]  # For x-axis
        # Plotting
        plt.plot(time_step, carbon_predicted, color='r', linestyle='--')
        plt.plot(time_step, carbon_realized, color='black')
        plt.xlabel('Time (hours)')
        plt.ylabel('Intensity')
        plt.title('Carbon Intensity {}'.format(date_iso))
        plt.legend(['Predicted', 'Realized'])
        plt.savefig('plots/carbon_{}.png'.format(date_iso))
        plt.show()
    return
