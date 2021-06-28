"""
PROJECT NAME
    ANALYZING AN ORGANIZATION’S PERFORMANCE TO PREDICT FUTURE STOCK MOVEMENT

FILE
    Utility File to house common Functions

GROUP DETAILS
    GROUP 1

TEAM MEMBERS
    Vasudev Madhuri	                   12010065
    Sonam Lakhe	                       12010044
    KaliPrasad Raghavendra Kuchibhotla 12010071
    Debjit Ray	                       12010066
    Ravikiran Ravinuthala	           12010045
"""

import requests
from sqlalchemy import create_engine

"""
Twitter input cleaner
"""
def format_search_tag(input_search_tag):
    """
    A routine to remove the hashtag.

    The below function will format the Search string
    that is passed to the program. If Searches for a Hash tag at the beginning
    of the string. if present does nothing, else will insert one.

    Args:
        input_search_tag (String): Industry/company name
    """
    find_hash = input_search_tag.find('#')
    if (find_hash < 0) or (find_hash > 0) :
        formated_search_tag = '#' + input_search_tag
    else:
        formated_search_tag = input_search_tag
    return formated_search_tag

"""
Get the Selenium web driver
"""
def get_driver(webdriver):
    """
    A routine to locate the Chrome web driver.

    The below function will locate the webdriver to be used by Selenium.

    Args:
        webdriver (object): Selenium webdriver handler
    """

    locationOfWebdriver = "chromedriver//chromedriver.exe"

    driver = webdriver.Chrome(locationOfWebdriver)
    return driver

"""
Identify the URL which holds the historic stock price
"""
def getStockURL(stockName,exchange, startDate, endDate):
    """
    A routine to form the URL.

    The below function will form the URL for the stock, exchange and 
    date range provided as input.

    Args:
        stockName (String): Industry/company name
        exchange (String) : Stock exchange where the company is listed
        startDate (String): Start date of the range of date for which we want to extract the prices
        endDate (String)  : End date of the range of date for which we want to extract the prices
    """
    stockHistory = ""
    link = "https://query2.finance.yahoo.com/v1/finance/search?q=" + stockName
    URL = requests.get(link).json()
    quotes = URL.get('quotes')
    
    # Go through each of the quotes and identify the exchange and symbol, we are searching for.
    for eachQuote in quotes:
        if eachQuote.get('exchange') == exchange:
            # One we have identified the exchange, we form the URL for getting the historical prices.
            symbol = eachQuote.get('symbol')
            stockHistory = "https://in.finance.yahoo.com/quote/" + symbol + "/history?period1=" + startDate + "&period2=" + endDate + "&interval=1d&filter=history&frequency=1d"
    return stockHistory

