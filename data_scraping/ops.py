#import .data_scraping
from parse import *
from scrape_yelp import *
import pickle

string = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns='  # fill in string values
pages = 162 # fill in last page of yelp browse data

dirty_data = scrap_yelp(string, pages)

df = parse_html(dirty_data)

with open('yelp_data.pickle', 'wb') as to_write:
    pickle.dump(df,to_write)
