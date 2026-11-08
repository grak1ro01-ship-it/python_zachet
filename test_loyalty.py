import unittest
from loyalty import apply_loyalty_discount, apply_3plus1


class TestLoyalty(unittest.TestCase):
    def setUp(self):
        self.coffee_items = [
            {"name": "Эспрессо", "price": 150, "category": "coffee"},
            {"name": "Капучино", "price": 200, "category": "coffee"},
            {"name": "Латте", "price": 250, "category": "coffee"},
            {"name": "Раф", "price": 300, "category": "coffee"}
        ]
        self.alcohol_items = [
            {"name": "Глинтвейн", "price": 350, "category": "alcohol"},
            {"name": "Сидр", "price": 250, "category": "alcohol"},
            {"name": "Пиво", "price": 300, "category": "alcohol"},
            {"name": "Пунш", "price": 400, "category": "alcohol"}
        ]

    def test_bronze_card(self):
        order = self.coffee_items[:3]
        result = apply_loyalty_discount(order, "Bronze")
        self.assertEqual(result["total"], 570.0)
        self.assertEqual(result["discount"], 30.0)

    def test_gold_card(self):
        result = apply_loyalty_discount(self.coffee_items, "Gold")
        self.assertEqual(result["total"], 637.5)
        self.assertEqual(result["discount"], 262.5)

    def test_no_card(self):
        order = self.coffee_items[:2]
        result = apply_loyalty_discount(order, "None")
        self.assertEqual(result["total"], 350.0)
        self.assertEqual(result["discount"], 0.0)

    def test_empty_and_alcohol(self):
        empty_res = apply_loyalty_discount([], "Gold")
        self.assertEqual(empty_res["total"], 0.0)

        alc_res = apply_loyalty_discount(self.alcohol_items, "Silver")
        self.assertEqual(alc_res["total"], 1170.0)
        self.assertEqual(alc_res["discount"], 130.0)

    def test_3plus1_four_items(self):
        discount, bonuses = apply_3plus1(self.coffee_items)
        self.assertEqual(discount, 150.0)
        self.assertEqual(len(bonuses), 1)

    def test_3plus1_three_items(self):
        discount, bonuses = apply_3plus1(self.coffee_items[:3])
        self.assertEqual(discount, 0.0)
        self.assertEqual(bonuses, [])


if __name__ == "__main__":
    unittest.main()
