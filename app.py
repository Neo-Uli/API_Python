from flask import Flask,jsonify,request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/productos')
def getProducts():
    return jsonify({"productos": products})

@app.route('/productos/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['sabor']==product_name]
    if (len(productsFound) > 0):
        return jsonify({"producto": productsFound[0]})
    return jsonify({"mensaje": "Producto no encontrado"})

@app.route('/productos', methods=['POST'])
def addProduct():
    new_product = {
        "nombre": request.json['sabor'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    products.append(new_product)
    return jsonify({"Productos": products, "mensaje": "Producto agregado"})

@app.route('/productos/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['sabor'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['sabor'] = request.json['sabor']
        productFound[0]['precio'] = request.json['precio']
        productFound[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "mensaje": "Producto actualizado",
            "Producto": productFound[0]
        })
    return jsonify({"mensaje": "Producto no encontrado"})

@app.route('/productos/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['sabor'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "mensaje": "Producto eliminado",
            "producto": products
        })
    return jsonify({"mensaje": "Producto no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
