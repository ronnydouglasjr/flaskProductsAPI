from flask import Flask, jsonify, request

app = Flask(__name__)

products = []


# Endpoint para criar um novo produto (POST)
@app.route('/products', methods=['POST'])
def createProduct():
    data = request.get_json()
    newProducts = {
        'id': len(products) + 1,
        'name': data['name'],
        'description': data['description'],
        'price': data['price'],
        'stock': data['stock']
    }
    products.append(newProducts)
    return jsonify(newProducts), 201


# Endpoint para obter todos os produtos (GET)
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products), 200


