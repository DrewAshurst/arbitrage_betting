# This is a sample Python script.
import requests


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




if __name__ == '__main__':

    print_hi('PyCharm')


    url = 'https://api.the-odds-api.com/v4/sports/basketball_ncaa'
    response = requests.get(url)
    responseContent = response.content

    responseContent = responseContent.strip()

    print(responseContent)




