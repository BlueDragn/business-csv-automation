from src.validator import validate_row

def process_data(data):
    valid_rows = []
    invalid_rows = []
    seen_order_ids = set()

    for row in data:
        errors = validate_row(row, seen_order_ids)

        if errors:
            invalid_rows.append({
                "row": row,
                "errors": errors
            })
        else:
            valid_rows.append(row)

    return valid_rows, invalid_rows
