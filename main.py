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

# Encontrar produto pelo ID
def findProductById(productID):
    for product in products:
        if product['id'] == productID:
            return product
    return None


# Endpoint para obter um produto específico (GET)
@app.route('/products/<int:productID>', methods=['GET'])
def getSpecificProduct(productID):
    product = findProductById(productID)
    if product:
        return jsonify(product), 200
    return jsonify('Produto não encontrado!'), 404


