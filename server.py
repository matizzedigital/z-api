from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Obtém os dados recebidos pelo webhook
    print("Dados recebidos:", data)
    
    # Aqui você pode processar os dados conforme necessário
    # Por exemplo, você pode extrair informações e tomar decisões com base nelas
    
    # Responda ao webhook (opcional)
    response = data
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)  # Inicia o servidor Flask em modo de depuração