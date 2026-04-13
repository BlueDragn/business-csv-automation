import csv
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:

            # skip empty rows
            if not any(row.values()):
                continue
            cleaned_row = {}
            for key, value in row.items():
                if value is not None:
                    cleaned_row[key] = str(value).strip()
                else:
                    cleaned_row[key] = value

            data.append(cleaned_row)
    return data
