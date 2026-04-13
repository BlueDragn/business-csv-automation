print("RUNNING NEW MAIN.PY")
from src.data_loader  import load_data
from src.processor import process_data
from src.reporter import generate_report



def main():

    data = load_data("input/messy_data.csv - Sheet1.csv")
    valid_rows, invalid_rows = process_data(data)
    generate_report(valid_rows, invalid_rows)

if __name__ == "__main__":
    main()