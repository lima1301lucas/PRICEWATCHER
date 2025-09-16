from scrapper import search
from notifier import send_alert
import json
PRODUCTS_FILE = "data/products.json"

def load_products():
    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    products = load_products()

    for product in products:
        name = product["name"]
        target_price = product["target_price"]

        print(f"Pesquisando: {name}")
        results = search(name, debug = True)

        for item in results:
            name = item["title"]
            price = item["price"]
            link = item["link"]

            if price <= target_price and price > 0:
                print(f"Alerta! {name} está por R$ {price:.2f}")
                send_alert(name, price, link)

if __name__ == "__main__":
    main()