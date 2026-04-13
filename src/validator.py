from  datetime import datetime

def validate_row(row, seen_order_ids):
    errors = []
    # ----------------ORDER ID ----------------------
    order_id = row.get("order_id")

    if not order_id or not order_id.strip():
        errors.append("missing_order_id")
    else:
        order_id = str(order_id).strip()
        row["order_id"] = order_id

        if order_id:
            if order_id in seen_order_ids:
                errors.append("duplicate Order ID")
            else:
                seen_order_ids.add(order_id)

    # ------------------- Email ----------------------
    email = row.get("customer_email")

    if not email or not email.strip():
        errors.append("missing_email")

    else:
        email = str(email.strip().lower())
        row["customer_email"] = email

        parts = email.split("@")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            errors.append("invalid_email")

    # ------------------- AMOUNT ----------------------
    amount = row.get("amount")

    if not amount or not str(amount).strip():
        errors.append("missing_amount")

    else:
        amount = str(amount).strip()

        cleaned_amount = ""
        for char in amount:
            if char.isdigit() or char == ".":
                cleaned_amount += char

    if not cleaned_amount:
        errors.append("invalid_amount")
    else:
        try:
            amount_value = float(cleaned_amount)
            if amount_value <= 0:
                errors.append("invalid_amount")
            else:
                row["amount"] = amount_value
        except ValueError:
            errors.append("invalid_amount")

    # ------------------- CURRENCY ----------------------
    currency = row.get("currency")

    if not currency or not currency.strip():
        errors.append("missing_currency")
    else:
        currency = currency.strip().upper()
        row["currency"] = currency

        allowed_currencies = {"INR", "USD", "EUR"}
        if currency not in allowed_currencies:
            errors.append("invalid_currency")

    # ------------------- ORDER DATE ----------------------
    order_date = row.get("order_date")

    if not order_date or not order_date.strip():
        errors.append("missing_order_date")

    else:
        order_date = str(order_date).strip()

        formats = ["%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%Y/%m/%d", "%d/%m/%Y"]
        parsed_date = None

        for fmt in formats:
            try:
                parsed_date = datetime.strptime(order_date, fmt)
                break
            except:
                continue

        if not parsed_date:
            errors.append("invalid_order_date")
        else:
            row["order_date"] = parsed_date.strftime("%Y-%m-%d")
    # ------------------- PAYMENT METHOD ----------------------
    payment_method = row.get("payment_method")

    if not payment_method or not payment_method.strip():
        errors.append("missing_payment_method")
    else:
        payment_method = payment_method.strip().lower()
        row["payment_method"] = payment_method

        allowed_payment_methods = {"upi", "card", "cash"}

        if payment_method not in allowed_payment_methods:
            errors.append("invalid_payment_method")

    # ------------------- BRANCH ID ----------------------
    branch_id = row.get("branch_id")
    if not branch_id or not str(branch_id).strip():
        errors.append("missing_branch_id")
    else:
        branch_id = str(branch_id).strip()
        row["branch_id"] = branch_id
    #--------------End------------------
    print(f"Row: {row}, Errors: {errors}")

    return errors









