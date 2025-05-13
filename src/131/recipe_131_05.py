from typing import TypedDict

class Item(TypedDict):
    title: str
    price: int
    in_stock: bool

product_data: Item = {"title": "えんぴつ", "price": 100, "in_stock": True}
