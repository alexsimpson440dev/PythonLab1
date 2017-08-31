__author__ = 'Alex'
#import statements for the request library

import urllib.request as request
import json

#gets the exchange rate from the base currency to the exchange requested from openexchangerates api

#API Documentation https://docs.openexchangerates.org/docs

def get_exchangeRate(baseCountry, exchangeCountry):

    #key for openexchangerates.org
    key = "23ecb3aa783e44408b0bdb3b46b1769e"

    exchangeURL = 'https://openexchangerates.org/api/latest.json?app_id=' + key + '&base=' + baseCountry
    #print(exchangeURL)   print if you want to show the url that is being used

    #Error handling for making a request to urllib
    #Reference: https://docs.python.org/3/tutorial/errors.html
    try:
        exchangeResponse = request.urlopen(exchangeURL)
    except Exception as e:
        print("Error making request", e)
        return

    try:
        #reads all information from the json url
        #Reference http://stackoverflow.com/questions/23049767/parsing-http-response-in-python
        exchangeResponseJson = exchangeResponse.read().decode('utf-8')

        #print if you want to print out all information that is read
        #helps debug
        #print(exchangeResponseJson)

        #parses the json to help read more precise data?
        parsed_json = json.loads(exchangeResponseJson)

        #uses parsed json and accesses sub-category 'rates' to get the exchange rate for a country
        #based on the base Country
        #reference: https://docs.openexchangerates.org/docs/latest-json
        exchangeRate = parsed_json['rates'][exchangeCountry]

    except Exception as e:
        print('Error processing response', e)
        return

    return exchangeRate

def main():
    #user input for the base country and exchange country then turns it to upper
    baseC = input('Enter in base exchange E.G - "USD" ').upper()
    exchangeC = input('Enter in Country you would like to get the rate for E.G - "EUR" ').upper()

    #gets the exchange rate for the base to the country chosen
    exchange = get_exchangeRate(baseC, exchangeC)
    if exchange is not None:
        print('The Exchange Rate from ' + baseC + ' to ' + exchangeC + ' is ' + str(exchange))
    else:
        print('Unable to get the exchange rate')

#runs main
main()

