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

# Endpoint para atualizar um produto (PUT)
@app.route('/products/<int:productID>', methods=['PUT'])
def updateProduct(productID):
    data = request.get_json()
    product = findProductById(productID)
    if product:
        product['name'] = data.get('name', product['name'])
        product['description'] = data.get('description', product['description'])
        product['price'] = data.get('price', product['price'])
        product['stock'] = data.get('stock', product['stock'])
        return jsonify({
            'mensagem': 'Produto atualizado com sucesso!',
            'produto': product
        }), 200
    return jsonify({'mensagem': 'Produto não encontrado!'}), 404

# Endpoint para deletar um produto (DELETE)
@app.route('/products/<int:productID>', methods=['DELETE'])
def deleteProduct(productID):
    product = findProductById(productID)
    if product:
        global products
        products = [p for p in products if p['id'] != productID]
        return jsonify('Produto removido com sucesso!'), 204


if __name__ == '__main__':
    app.run(debug=True)

