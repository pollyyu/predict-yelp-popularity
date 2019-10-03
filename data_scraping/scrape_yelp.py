
import requests
import time
import random


def scrap_yelp(string, pages) :
    ugly_data = {}

    for i in range(1, pages + 1) :
        url = string + str(i)
        response = requests.get(url)
        ugly_data['page_' + str(i)] = response.text

        time.sleep(.5 + 2 * random.random())

    return ugly_data
