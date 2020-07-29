import requests
import json
from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer

# get mentions from all SUBMISSIONS in ALL subreddits
def s_getPushshiftData_all(query, after, before, frequency):
    url = 'https://api.pushshift.io/reddit/search/submission/?q=' + str(query) + '&after=' + str(after) + '&before=' + str(before) + '&aggs=created_utc&frequency=' + str(frequency) + '&size=0'
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    #print(data['aggs']['created_utc'])
    return data['aggs']['created_utc']

# get mentions from all SUBMISSIONS in ONE subreddit
def s_getPushshiftData_bySub(query, after, before, frequency, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?q=' + str(query) + '&after=' + str(after) + '&before=' + str(before) + '&aggs=created_utc&frequency=' + str(frequency) + '&size=0' + '&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    #print(data['aggs']['created_utc'])
    return data['aggs']['created_utc']

# get mentions from all COMMENTS in ALL subreddits
def c_getPushshiftData_all(query, after, before, frequency):
    url = 'https://api.pushshift.io/reddit/search/comment/?q=' + str(query) + '&after=' + str(after) + '&before=' + str(before) + '&aggs=created_utc&frequency=' + str(frequency) + '&size=0'
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    #print(data['aggs']['created_utc'])
    return data['aggs']['created_utc']

# get mentions from all COMMENTS in ONE subreddit
def c_getPushshiftData_bySub(query, after, before, frequency, sub):
    url = 'https://api.pushshift.io/reddit/search/comment/?q=' + str(query) + '&after=' + str(after) + '&before=' + str(before) + '&aggs=created_utc&frequency=' + str(frequency) + '&size=0' + '&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    #print(data['aggs']['created_utc'])
    return data['aggs']['created_utc']


def main():
    # to convert unix to utc and vice versa
    # https://www.unixtimestamp.com/index.php

    # after: 1546300800 (01/01/2019)
    # before: 1577750400 (12/31/2019)

    # query for submissions by subreddit
    s_subreddit_name_data = s_getPushshiftData_bySub("tesla", 1546300800, 1577750400, "day", "wallstreetbets")
    s_subreddit_ticker_data = s_getPushshiftData_bySub("tsla", 1546300800, 1577750400, "day", "wallstreetbets")

    # query for comments by subreddit
    c_subreddit_name_data = c_getPushshiftData_bySub("tesla", 1546300800, 1577750400, "day", "wallstreetbets")
    c_subreddit_ticker_data = c_getPushshiftData_bySub("tsla", 1546300800, 1577750400, "day", "wallstreetbets")


    # output to excel file
    conv = Converter()
    conv.convert(s_subreddit_name_data, Writer(file='/Users/hannahvu/desktop/s_subreddit_name_data.xlsx')) # get mentions of full company name
    conv.convert(s_subreddit_ticker_data, Writer(file='/Users/hannahvu/desktop/s_subreddit_ticker_data.xlsx')) # get mentions of ticker name

    conv.convert(c_subreddit_name_data, Writer(file='/Users/hannahvu/desktop/c_subreddit_name_data.xlsx')) # get mentions of full company name
    conv.convert(c_subreddit_ticker_data, Writer(file='/Users/hannahvu/desktop/c_subreddit_ticker_data.xlsx')) # get mentions of ticker name

main()
