from flask import Flask, render_template

app = Flask(__name__)

# Add ID to each product
products = [
    {
        "id": 0,
        "name": "Metformin XR",
        "image": "Metformin.jpg",
        "dosage": "750mg",
        "price": "AUD 14.80",
        "form": "Tablet",
        "description": "For blood sugar control",
        "category": "Diabetes",
        "source": "https://www.adiuvopharma.com/en/categorias-2/antidiabeticos/metformina-750-xr-y-850/",
        "usage": "Take once daily with meals or as directed by your doctor.",
        "ingredients": "Metformin Hydrochloride",
        "storage": "Store below 25°C. Keep away from moisture and direct sunlight.",
        "warning": "Consult your doctor before use if you have kidney problems.",
        "rating": 4.4,
        "num_reviews": 920,
        "discount": 15,
        "sold_quantity": "1.2k"
    },
    {
        "id": 1,
        "name": "Voltaren Emulgel",
        "image": "Voltaren.jpg",
        "dosage": "150g",
        "price": "AUD 18.90",
        "form": "Gel",
        "description": "Anti-inflammatory for muscle pain",
        "category": "Anti-inflammatory",
        "source": "https://www.pharmaplaza.hu/voltaren-emulgel-forte-20mgg-gel-150g",
        "usage": "Apply to the affected area 3 to 4 times a day.",
        "ingredients": "Diclofenac diethylammonium",
        "storage": "Store below 30°C. Do not freeze.",
        "warning": "Avoid contact with eyes or mucous membranes. Do not apply to broken skin.",
        "rating": 4.6,
        "num_reviews": 1380,
        "discount": 10,
        "sold_quantity": "2.4k"
    },
    {
        "id": 2,
        "name": "BurnAid Gel",
        "image": "Burnaid.jpg",
        "dosage": "25g",
        "price": "AUD 6.50",
        "form": "Gel",
        "description": "First-aid burn relief",
        "category": "Burn",
        "source": "https://www.chemistwarehouse.com.au/buy/31066/Burnaid-Burn-Gel-25g",
        "usage": "Apply liberally to burn area. Do not rub in.",
        "ingredients": "Melaleuca Oil, Water Gel Base",
        "storage": "Store below 25°C. Keep tube tightly closed.",
        "warning": "For external use only. Seek medical advice for serious burns.",
        "rating": 4.1,
        "num_reviews": 430,
        "discount": None,
        "sold_quantity": "870"
    },
    {
        "id": 3,
        "name": "Panadol",
        "image": "Panadol.jpeg",
        "dosage": "500mg",
        "price": "AUD 5.00",
        "form": "Tablet",
        "description": "Pain relief and fever reduction",
        "category": "Internal Medicine",
        "source": "https://onlinepharmacyuk.co.uk/medicines-treatments/pain-relief/panadol-advance-500mg-tablets-16",
        "usage": "Take 1-2 tablets every 4-6 hours as needed.",
        "ingredients": "Paracetamol",
        "storage": "Store below 30°C. Protect from light.",
        "warning": "Do not exceed 8 tablets in 24 hours. Overdose may cause liver damage.",
        "rating": 4.8,
        "num_reviews": 2100,
        "discount": 5,
        "sold_quantity": "3.1k"
    },
    {
        "id": 4,
        "name": "Betadine Solution",
        "image": "Betadine.jpg",
        "dosage": "250ml",
        "price": "AUD 12.90",
        "form": "Liquid",
        "description": "Antiseptic for wounds",
        "category": "Trauma Care",
        "source": "https://yms.co.za/product/betadine-antiseptic-solution-250ml/",
        "usage": "Apply directly to the affected area. Do not dilute.",
        "ingredients": "Povidone-iodine",
        "storage": "Store below 25°C. Keep away from heat and sunlight.",
        "warning": "Avoid use if allergic to iodine. Not for prolonged use.",
        "rating": 4.0,
        "num_reviews": 500,
        "discount": None,
        "sold_quantity": "650"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/products')
def all_products():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return "Product not found", 404
    return render_template('product_details.html', product=product)

@app.route('/delivery')
def delivery():
    return render_template('delivery_request.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)