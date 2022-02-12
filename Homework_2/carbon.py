import datetime
import json
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


# def query_carbon(date=get_current_day(), use_cache=True):
#     if use_cache is True:
#     headers = {
#         'Accept': 'application/json'
#     }
#     data = requests.get('https://api.carbonintensity.org.uk/intensity/date/{date}', params={date}, headers = headers)
#     print(data.json())
#     if use_cache is False:
def query_carbon(date_today=get_current_day(), use_cache=True):
    file_exists = True
    if not os.path.isdir("/Users/Boom/PycharmProjects/ME499-WIN22/Homework_2/data"):
        os.mkdir("data")
        file_exists = False
    if use_cache and file_exists is True:
        print("Used cache file to get data")
        file = open('/Users/Boom/PycharmProjects/ME499-WIN22/Homework_2/data/carbon 2019-10-31.json')
        data = json.load(file)
        # fprint(data)
        # for i in data:
        #     print(i)
        print(data)
        file.close()
        return {}
    else:
        print(date_today)
        headers = {'Accept': 'application/json'}

        new_date = 'https://api.carbonintensity.org.uk/intensity/date/{}'.format(date_today)
        requested_data = requests.get(new_date, params={}, headers=headers)  # could get block if run too much
        print(requested_data.status_code)
        print(requested_data.json())
        requested_data.json()
        return {}


if __name__ == '__main__':
    print(get_current_day())
    date = datetime.date.today()
    # with open("carbon 2019-10-31.json", "r") as infile:
    #     data = json.load(infile)
    # query_carbon(date)
    query_carbon()
