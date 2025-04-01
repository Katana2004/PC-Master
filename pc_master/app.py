from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Настройки языка
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(locale_selector=lambda: request.args.get('lang', 'en'))

# Переводы
translations = {
    "en": {
        "title": "PC Master",
        "catalog": "View Catalog",
        "welcome": "Welcome to PC Master!",
        "contacts": "Contact Us",
        "phone": "Phone",
        "email": "Email"
    },
    "de": {
        "title": "PC Master",
        "catalog": "Katalog anzeigen",
        "welcome": "Willkommen bei PC Master!",
        "contacts": "Kontaktieren Sie uns",
        "phone": "Telefon",
        "email": "E-Mail"
    }
}

# Пример данных продуктов
products = [
    {"id": 1, "name": "Gaming PC", "desc": "High-performance gaming PC", "price": "$1200", "img": "gaming_pc.jpg"},
    {"id": 2, "name": "Office PC", "desc": "Reliable office PC", "price": "$800", "img": "office_pc.jpg"},
    {"id": 3, "name": "Mini PC", "desc": "Compact and powerful mini PC", "price": "$600", "img": "mini_pc.jpg"}
]

@app.route("/")
def home():
    lang = request.args.get('lang', 'en')
    return render_template("index.html", t=translations.get(lang, translations['en']), lang=lang)

@app.route("/products")
def product_list():
    lang = request.args.get('lang', 'en')
    return render_template("products.html", products=products, t=translations.get(lang, translations['en']), lang=lang)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    lang = request.args.get('lang', 'en')
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template("product_detail.html", product=product, t=translations.get(lang, translations['en']), lang=lang)

@app.route("/contacts")
def contacts():
    lang = request.args.get('lang', 'en')
    return render_template("contacts.html", t=translations.get(lang, translations['en']), lang=lang)

if __name__ == "__main__":
    app.run(debug=True)