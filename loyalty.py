Discounts = {
    "Bronze": 0.05,
    "Silver": 0.10,
    "Gold": 0.15,
    "None": 0.0
}

def apply_3plus1(items):
    if not items or len(items) < 4:
        return 0.0, []

    non_alcohol = []
    for item in items:
        if item.get("category") != "alcohol":
            non_alcohol.append(item)

    if len(non_alcohol) < 4:
        return 0.0, []

    cheapest = non_alcohol[0]
    for item in non_alcohol:
        if item["price"] < cheapest["price"]:
            cheapest = item

    discount = float(cheapest["price"])
    bonuses = ["Акция 3+1: бесплатный напиток " + cheapest["name"]]
    return discount, bonuses


def apply_loyalty_discount(items, card_level):
    if not items:
        return {"total": 0.0, "discount": 0.0, "bonuses": []}

    total_price = 0.0
    for item in items:
        total_price += item["price"]

    bonus_discount, bonuses = apply_3plus1(items)
    price_after_bonus = total_price - bonus_discount
    if price_after_bonus < 0:
        price_after_bonus = 0.0

    rate = Discounts.get(card_level, 0.0)
    card_discount = price_after_bonus * rate

    if card_discount > 0:
        bonuses.append("Скидка по карте " + str(card_level))

    total_discount = bonus_discount + card_discount
    final_total = total_price - total_discount
    if final_total < 0:
        final_total = 0.0

    return {
        "total": round(final_total, 2),
        "discount": round(total_discount, 2),
        "bonuses": bonuses
    }
