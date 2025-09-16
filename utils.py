import re

def parse_price(price_str: str) -> float:
    if not price_str:
        return 0.0

    cleaned = re.sub(r'[^\d,\.]', '', price_str)
    if ',' in cleaned and cleaned.count(',') == 1 and '.' not in cleaned:
        cleaned = cleaned.replace(',', '.')
    try:
        return float(cleaned)
    except ValueError:
        return 0.0
