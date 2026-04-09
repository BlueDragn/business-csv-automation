import data_loader


loaded_data = data_loader.data_loader()


seen_order_ids = set()
for row in loaded_data:
    error = []

    order_id = row.get('order_id')
    #Rule 1: Order ID should not be empty:Required
    if not order_id:
        error.append("Order ID is missing")

    #Rule 2: Order ID should be unique
    if order_id:
        if order_id in seen_order_ids:
            error.append("duplicate Order ID")
        else:
            seen_order_ids.add(order_id)
