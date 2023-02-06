# This is a sample Python script.
import requests
from bs4 import BeautifulSoup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




if __name__ == '__main__':

    print_hi('PyCharm')


    url = 'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=1268ceecd3baff09507cfb926d3ce10c&regions=us&markets=h2h&oddsFormat=american'
    response = requests.get(url)
    responseContent = response.content
    responseText = BeautifulSoup(responseContent, 'html.parser')
    parseText = responseText.get_text()


    print(parseText)



