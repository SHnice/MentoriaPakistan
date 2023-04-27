class DiscountCalculator:
    def __init__(self, items):
        self.discounted_items = [DiscountedItem(item) for item in items]
    
    def apply_discount(self, item_name, discount):
        for discounted_item in self.discounted_items:
            if discounted_item.name == item_name:
                discounted_item.discount = discount
    
    def get_discounted_items(self):
        return self.discounted_items