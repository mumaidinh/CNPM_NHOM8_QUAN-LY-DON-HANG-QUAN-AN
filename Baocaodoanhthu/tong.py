def report_revenue(orders, report_type, date_value):
    revenue = 0

    for order in orders:
        if report_type == "day" and order["date"] == date_value:
            revenue += order["total"]
        elif report_type == "month" and order["date"].startswith(date_value):
            revenue += order["total"]

    return revenue