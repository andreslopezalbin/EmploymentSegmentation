
import logging as logger
import csv


class Preprocessor:
    genderHeader = ''
    genders = {'Ambos sexos': 0, 'Hombres': 1, 'Mujeres': 2}
    ages = {
        'Total': 0,
        'Menores de 25 años': 1,
        '25 y más años': 2,
        'De 16 a 19 años': 3,
        'De 20 a 24 años': 4,
        'De 25 a 54 años': 5,
        '55 y más años': 6}
    regions = {
        'Total Nacional': 0,
        'Andalucía': 1,
        'Aragón': 2,
        'Asturias': 3,
        'Balears, Illes': 4,
        'Canarias': 5,
        'Cantabria': 6,
        'Castilla y León': 7,
        'Castilla - La Mancha': 8,
        'Cataluña': 9,
        'Comunitat Valenciana': 10,
        'Extremadura': 11,
        'Galicia': 12,
        'Madrid': 13,
        'Murcia, Región de': 14,
        'Navarra': 15,
        'País Vasco': 16,
        'La Rioja': 17,
        'Ceuta': 18,
        'Melilla': 19
    }

    def __init__(self):
        logger.getLogger().setLevel(logger.INFO)
        logger.basicConfig(format='%(levelname)s: %(message)s')
        logger.info('Starting')
        # logging.error('Error')

        with open('./data/dataset.csv', encoding="utf8") as infile, open("./data/train.csv", "w", newline='', encoding="utf8") as outfile, open("./data/rawTrainDataset.csv", "w", newline='', encoding="utf8") as outfileRaw:
            readCSV = csv.reader(infile, delimiter=';')
            writerCSV = csv.writer(outfile, delimiter=';')
            writerRaw = csv.writer(outfileRaw, delimiter=';')
            ageHeader = []
            termHeader = []
            totalObjects = 0
            writerCSV.writerow(
                ['Comunidad Autonoma', 'Tasa Paro', 'Sexo', 'Periodo', 'Edad'])
            writerRaw.writerow(
                ['Comunidad Autonoma', 'Tasa Paro', 'Sexo', 'Periodo', 'Edad'])
            for i, row in enumerate(readCSV):
                if i == 0:
                    ageHeader = row
                    continue  # Skip first line
                if i == 1:
                    termHeader = row
                    continue

                if not self.checkNewGender(row[0]):
                    for z, column in enumerate(row):
                        if z == 0:
                            continue  # skip first column
                        totalObjects += 1

                        writerCSV.writerow(
                            [self.regions[row[0]], column, self.genders[self.genderHeader], termHeader[z], self.ages[ageHeader[z]]])

                        writerRaw.writerow(
                            [row[0], column, self.genderHeader, termHeader[z], ageHeader[z]])

            logger.info('Finished with %s objects', totalObjects)

    def checkNewGender(self, firstColumn):
        result = False
        if firstColumn in self.genders:
            self.genderHeader = firstColumn
            logger.info('New gender: %s', self.genderHeader)
            result = True
        return result


if __name__ == '__main__':
    Preprocessor()
