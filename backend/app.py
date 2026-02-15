from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample restaurant menu data
menu_items = [
    {"name": "Paneer Butter Masala", "description": "Creamy paneer curry with rich tomato gravy", "price": 220},
    {"name": "Veg Biryani", "description": "Aromatic basmati rice cooked with vegetables and spices", "price": 180},
    {"name": "Masala Dosa", "description": "Crispy dosa with spicy potato filling", "price": 120},
    {"name": "Veg Manchurian", "description": "Fried veg balls tossed in Indo-Chinese sauce", "price": 150},
    {"name": "Gulab Jamun", "description": "Soft sweet dessert (2 pieces)", "price": 60}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Restaurant backend is running!"})

@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(menu_items)

if __name__ == "__main__":
    app.run(debug=True)
