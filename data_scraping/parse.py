import pandas as pd
from bs4 import BeautifulSoup
import json
from collections import defaultdict

def parse_html(ugly_data):

    df = pd.DataFrame(columns = ['name', 'parentBusiness', 'reviewCount', 'neighborhoods', 'rating',
           'priceRange', 'formattedAddress', 'phone', 'categories'])


    for i, values in ugly_data.items():
        print(i)
        soup = BeautifulSoup(ugly_data[i], "lxml")

        # where the json snippet is found in the html
        to_parse = soup.find_all(type='application/json')

        # get just the json snippet in string format
        test = str(to_parse).split('<!--')[1].split('-->')[0]

        # transform string to json so that we can read
        read_json = json.loads(test)

        # get the section of the json where all my business information is located
        to_loop = read_json['searchPageProps']['searchResultsProps']['searchResults']

        # loop in a page to get business
        business = loop_in_page(to_loop)

        # get data within each business
        df = df.append(business_info(business))
    return df

def loop_in_page(to_loop):
    business = {}

    for i, values in enumerate(to_loop):
        nu = int(i + 1)

        try:
            results = to_loop[nu]['searchResultBusiness']
            business[nu] = results
        except:
            pass

    return business

def business_info(business):
    my_dict = defaultdict(list)

    for i, values in business.items():

        # categories are nested dict so loop through that first
        categories = values['categories'][:]

        cat = {}
        for index, value in enumerate(categories):
            key = str(index+1)
            cat[key] = value['title']


        # now, inserting values to my dict
        my_dict['name'].append(values['name'])
        my_dict['parentBusiness'].append(values['parentBusiness'])

        my_dict['reviewCount'].append(values['reviewCount'])
        my_dict['neighborhoods'].append(values['neighborhoods'])
        my_dict['rating'].append(values['rating'])
        my_dict['priceRange'].append(values['priceRange'])
        my_dict['formattedAddress'].append(values['formattedAddress'])
        my_dict['phone'].append(values['phone'])
        my_dict['categories'].append(list(cat.values()))

    return pd.DataFrame(my_dict)

    # these are other features I chose to exclude because are mostly null
        #     print(values['businessUrl'])
        #     print(values['alternateNames'])
        #     print(values['serviceArea'])