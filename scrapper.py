from playwright.sync_api import sync_playwright
from utils import parse_price, clean_store
import urllib.parse


def search(product_name: str, debug: bool = True):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=not debug,
            slow_mo=1000 if debug else 0
        )

        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})
        query = urllib.parse.quote(product_name)
        link_home = "https://www.zoom.com.br"
        url = f"{link_home}/search?q={query}"
        page.goto(url, wait_until="networkidle")

        try:
            page.wait_for_selector("div.Hits_ProductCard__Bonl_", timeout=8000)
            item = page.query_selector("div.Hits_ProductCard__Bonl_")

            search_product = item.query_selector("a")
            search_product = search_product.get_attribute("href") if search_product else ""
            link_product = f"{link_home}{search_product}"
            page.goto(link_product)

            page.wait_for_selector("div.Title_Name__fFJe6.Hero_Title__9u24V", timeout=8000)

            title_element = page.query_selector('div.Title_Name__fFJe6 h1')
            price_element = page.query_selector('div.Price_ValueContainer__ndCqK strong')
            store_element = page.query_selector('span.Price_Merchant__wPTJn span')

            title = title_element.inner_text() if title_element else product_name
            price = parse_price(price_element.inner_text() if price_element else "")
            store = clean_store(store_element.inner_text() if store_element else "")

            results.append({
                "title": title,
                "price": price,
                "store": store,
                "link": link_product
            })

        except Exception as e:
            print(f"[ERRO] Falha ao buscar produto '{product_name}': {e}")

        browser.close()

    return results