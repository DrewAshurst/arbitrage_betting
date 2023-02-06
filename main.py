import dataCollection
import dataLocaters


def main():
    dataCollection.createCsv()
    bets = dataLocaters.findBestBets()
    for i in bets:
        print(i)


main()
