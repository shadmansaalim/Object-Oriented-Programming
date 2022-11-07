import csv


class Airlines:
    def __init__(self) -> None:
        self.aircrafts = None
        self.load_aircrafts_data('./data/aircraft.csv')

    def load_aircrafts_data(self, file_path):
        with open(file_path, 'r') as file:
            lines = csv.reader(file)
            # Ignoring the header with next method
            header = next(lines)
            for line in lines:
                print(line)
        file.close()


Airlines()
