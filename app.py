from flask import Flask, render_template, abort
import random

app = Flask(__name__)

# Generate 50+ sample products
product_names = [
    "iPhone 15", "Samsung Galaxy S24", "Sony WH-1000XM5 Headphones", "MacBook Air M2", "Boat Airdopes 441",
    "OnePlus Nord CE 3 Lite", "ASUS TUF Gaming Laptop", "Canon EOS 1500D DSLR", "Redmi Note 13 Pro+",
    "Realme Narzo 60", "HP Pavilion x360", "Logitech MX Master 3S", "Samsung Galaxy Watch 6",
    "Apple Watch Series 9", "Acer Aspire 7", "Dell XPS 13", "Lenovo Legion 5 Pro", "JBL Flip 6 Speaker",
    "Fire-Boltt Ninja Call Pro", "Mi Smart Band 7", "Oppo A78 5G", "Vivo V27 Pro", "Nikon D3500 DSLR",
    "Honor Pad 8", "Samsung Galaxy Tab S9", "Realme Buds Wireless 3", "boAt Rockerz 255 Pro+",
    "Philips Air Fryer", "Prestige Mixer Grinder", "Apple Mac Studio", "Sony PlayStation 5", "Xbox Series X",
    "LG OLED TV", "Mi 4K Smart TV", "Samsung Refrigerator", "IFB Washing Machine", "Dyson V11 Vacuum Cleaner",
    "Syska LED Bulb", "TP-Link WiFi Router", "Asus ROG Phone 8", "Nothing Phone 2",
    "Motorola Edge 40", "TCL Android TV", "Haier AC 1.5 Ton", "Blue Star Water Purifier",
    "Sony Alpha ZV-E10", "Bose QuietComfort Earbuds II", "Jabra Elite 4 Active", "Asus Chromebook Flip",
    "HP LaserJet Printer", "Canon PIXMA G3000"
]

products = []
for i, name in enumerate(product_names, 1):
    products.append({
        "id": i,
        "name": name,
        "price": random.randint(1500, 150000),
        "image": f"https://via.placeholder.com/200x200.png?text={'+'.join(name.split())}"
    })

@app.route('/')
def user_dashboard():
    return render_template('user_dashboard.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)