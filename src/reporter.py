import os
import csv

def generate_report(valid_rows, invalid_rows):

    os.makedirs("output", exist_ok=True)

    # -------------- CLEAN DATA -----------------
    if valid_rows:
        with open('output/clean_data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = valid_rows[0].keys())
            writer.writeheader()
            writer.writerows(valid_rows)

    # -------------- ERROR REPORT -----------------
    with open("output/rejected.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # header
        writer.writerow(["row", "errors"])

        for item in invalid_rows:
            writer.writerow([item["row"], ", ".join(item["errors"])])

    # -------------- SUMMARY REPORT -----------------
    total_rows = len(valid_rows) + len(invalid_rows)

    print("\n-- REPORT SUMMARY --")
    print("Total rows:", total_rows)
    print("Valid rows:", len(valid_rows))
    print("Invalid rows:", len(invalid_rows))
