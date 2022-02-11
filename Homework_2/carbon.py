import datetime
import json

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


def query_carbon:



if __name__ == '__main__':
    print(get_current_day())
    with open("carbon.json", "r") as infile:
        in_data = json.load(infile)

    print(in_data['data'])
