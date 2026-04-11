import data_loader
from  datetime import datetime

loaded_data = data_loader.data_loader()


seen_order_ids = set()
for row in loaded_data:
    errors= []

    # Order ID Validation
    order_id = row.get('order_id')
    #Rule 1: Order ID should not be empty:Required
    if not order_id:
        errors.append("Order ID is missing")
    else:
        order_id = order_id.strip()
        row["order_id"] = order_id

    #Rule 2: Order ID should be unique
    if order_id:
        if order_id in seen_order_ids:
            errors.append("duplicate Order ID")
        else:
            seen_order_ids.add(order_id)


    # Email Validation
    email = row.get("customer_email")
    #Rule 1: Email should not be empty:Required
    if not email:
        errors.append("missing_email")
    #Rule 2: Email should be in a valid format
    if email:
        email = email.strip().lower()
        row["customer_email"] = email
        
        if "@" not in email or "." not in email.split("@")[-1]:
            errors.append("invalid_email")


    # Price Validation
    amount = row.get("amount")
    #Rule 1: Price should not be empty:Required
    if not amount:
        errors.append("missing_amount")
    #Rule 2: Price should be a positive number
    if amount:

        amount = str(amount).strip()

        cleaned_amount = ""

        for char in amount:
            if char.isdigit() or char == ".":
                cleaned_amount += char
        try:
            amount_value = float(cleaned_amount)
            if amount_value <= 0:
                errors.append("invalid_amount")
            row["amount"] = amount_value
        except ValueError:
            errors.append("invalid_amount")

    if not cleaned_amount:
        errors.append("invalid_amount")
    else:
        try:
            amount_value = float(cleaned_amount)
            if amount_value <= 0:
                errors.append("invalid_amount")
            row["amount"] = amount_value
        except ValueError:
            errors.append("invalid_amount")


    # Currency Validation
    currency = row.get("currency")
    #Rule 1: Currency should not be empty:Required
    if not currency or not currency.strip():
        errors.append("missing_currency")
    else:
        currency = currency.strip().upper()
        row["currency"] = currency

        allowed_currencies = {"INR", "USD", "EUR"}

        if currency not in allowed_currencies:
            errors.append("invalid_currency")


    # Order Date Validation
    order_date = row.get("order_date")
    #Rule 1: Order Date should not be empty:Required
    if not order_date or not order_date.strip():
        errors.append("missing_order_date")
    #Rule 2: Order Date should be in a valid format (YYYY-MM-DD)
    if order_date:
        order_date = order_date.strip()

        parsed_date = None

        formats = ["%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%Y/%m/%d", "%d/%m/%Y"]

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



    # Payment Method Validation
    payment_method = row.get("payment_method")

    if payment_method and payment_method.strip():
        payment_method = payment_method.strip().lower()
        row["payment_method"] = payment_method

        allowed_payment_methods = {"upi", "card", "cash"}

        if payment_method not in allowed_payment_methods:
            errors.append("invalid_payment_method")

    # Branch Id
    branch_id = row.get("branch_id")
    if not branch_id or not branch_id.strip():
        errors.append("missing_branch_id")
    else:
        branch_id = branch_id.strip()
        row["branch_id"] = branch_id


    print(f"Row: {row}, Errors: {errors}")



