def get_label(title: str, price: int, is_stock: bool) -> str:
    stock_text = "在庫あり" if is_stock else "在庫なし"    
    return f"{title}：{price}円 {stock_text}"
