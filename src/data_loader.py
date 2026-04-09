import csv
def data_loader():
    data = []
    with open('input/messy_data.csv - Sheet1.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:

            # skip empty rows
            if not any(row.values()):
                continue
            cleaned_row = {}
            for key, value in row.items():
                if value:
                    cleaned_row[key] = value.strip()
                else:
                    cleaned_row[key] = value

            data.append(cleaned_row)
    return data
