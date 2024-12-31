def format_currency(value, add_decimal=False):
    formatted_value = f"R$ {int(value):,}".replace(",", ".")
    if add_decimal:
        formatted_value += ",00"
    return formatted_value
