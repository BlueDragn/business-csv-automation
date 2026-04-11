import data_loader


loaded_data = data_loader.data_loader()


seen_order_ids = set()
for row in loaded_data:
    errors= []

    # Order ID Validation
    order_id = row.get('order_id')
    #Rule 1: Order ID should not be empty:Required
    if not order_id:
        errors.append("Order ID is missing")

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


    # Currency Validation

    currency = row.get("currency")
    #Rule 1: Currency should not be empty:Required
    if not currency:
        errors.append("missing_currency")
    #Rule 2: Currency should be a valid ISO 4217 code
    if currency:
        currency = currency.strip().upper()
        row["currency"] = currency

        allowed_currencies = {"INR", "USD", "EUR"}

        if currency not in allowed_currencies:
            errors.append("invalid_currency")







    print(f"Row: {row}, Errors: {errors}")



