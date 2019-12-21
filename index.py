import logging as logger
import csv

genderHeader = ''


def main():
    logger.getLogger().setLevel(logger.INFO)
    logger.basicConfig(format='%(levelname)s: %(message)s')
    logger.info('Starting')
    # logging.error('Error')

    with open('./data/dataset.csv') as infile, open("./data/cleanedDataset.csv", "w", newline='') as outfile:
        readCSV = csv.reader(infile, delimiter=';')
        writerCSV = csv.writer(outfile, delimiter=';')
        ageHeader = []
        termHeader = []
        ageLabel = ''

        for i, row in enumerate(readCSV):
            if i == 0:
                ageHeader = row
                continue  # Skip first line
            if i == 1:
                termHeader = row
                continue

            if not checkNewGender(row[0]):
                for z, column in enumerate(row):
                    # logger.info(column)
                    if z == 5:
                        break
                    writerCSV.writerow([row[0], column, genderHeader, termHeader[z]])
                if i == 25:
                    break
        # logger.info('Age Header: %s', ageHeader)
        # logger.info('Term Header: %s ', termHeader)


def checkNewGender(firstColumn):
    genders = ['Ambos sexos', 'Hombres', 'Mujeres']
    if firstColumn in genders:
         global genderHeader
         genderHeader = firstColumn
         logger.info('gender: %s', genderHeader)
         return True
    else:
        return False


if __name__ == '__main__':
    main()
