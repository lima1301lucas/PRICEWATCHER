import os
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_alert(product_name: str, price: float, link: str):
    message = (
        f"⚠️ OFERTA\n"
        f"Produto: {product_name}\n"
        f"Preço encontrado: R$ {price:.2f}\n"
        f"Link: {link}"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    response = requests.post(url, data = payload)
    return response.status_code == 200