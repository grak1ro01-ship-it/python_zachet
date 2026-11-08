bronze_level = 1
silver_level = 2
gold_level = 3

bronze_discount = 0.05
silver_discount = 0.10
gold_discount = 0.15
no_discount = 0


def calculate_discount(price, loyalty_level):
    if loyalty_level == bronze_level:
        discount = price * bronze_discount
    elif loyalty_level == silver_level:
        discount = price * silver_discount
    elif loyalty_level == gold_level:
        discount = price * gold_discount
    else:
        discount = no_discount

    return max(0, price - discount)