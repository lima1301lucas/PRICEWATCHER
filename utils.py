import re

def parse_price(price_str: str) -> float:
    if not price_str:
        return 0.0

    cleaned = re.sub(r'[^\d,]', '', price_str)
    cleaned = cleaned.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

def clean_store(store_name: str) -> str:
    if not store_name:
        return ""

    cleaned = re.sub(r'^\s*via\s+', '', store_name, flags=re.IGNORECASE).strip()
    return cleaned