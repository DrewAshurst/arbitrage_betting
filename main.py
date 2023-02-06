import dataCollection
import dataLocaters
import csv


def main():
    dataCollection.createCsv()
    data = dataLocaters.findGames()
    
    with open('collegeBasketball.csv', 'w', newline='') as f:  # You will need 'wb' mode in Python 2.x
        for i in data:
            data[i]['game'] = i
        w = csv.DictWriter(f, data[i].keys())
        w.writeheader()
        for i in data:
            w.writerow(data[i])
    


main()
