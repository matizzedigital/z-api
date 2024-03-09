from flask import Flask, request, jsonify
from zapi import WhatsAppAPI
from APIGoogleSheets import GoogleSheetsAPI

# Configurações
SAMPLE_SPREADSHEET_ID = '1oREYpTbM1lfUdv6aHssajVRqfRDZQLi9w7Y9wZgtzJg'
SAMPLE_RANGE_NAME = 'Dados!A1:D146'

# Cria uma instância da classe GoogleSheetsAPI
api = GoogleSheetsAPI(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)

wpp = WhatsAppAPI("5527992987369", "3CBF0E47A1C1F0D629718ABF5D20188A", "DDE2AA3AF96DEFD1471EC1ED", "F90a743cd9f1f4abea1fa94b878c0b2bcS")

app = Flask(__name__)

host = "0.0.0.0"
wpp = WhatsAppAPI("5527992987369", "3CBF0E47A1C1F0D629718ABF5D20188A", "DDE2AA3AF96DEFD1471EC1ED", "F90a743cd9f1f4abea1fa94b878c0b2bcS")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Obtém os dados recebidos pelo webhook
    print("Dados recebidos:", data)

    # Aqui você pode processar os dados conforme necessário
    # Por exemplo, você pode extrair informações e tomar decisões com base nelas

    # Responda ao webhook (opcional)

    senderName = data["senderName"]
    message = data["text"]["message"]
    optionchoice = data["listResponseMessage"]["title"]

    if message == "AUTO":
        wpp.sendText(f'{message}')
        wpp.sendText(f'Olá, {senderName}. Bem vindo ao sistema de atendimento do nosso gestor de condomínios')
        option = [
            {
                "id": "1",
                "title": "Setor 1"
            },
            {
                "id": "2",
                "title": "Setor 2"
            },
            {
                "id": "3",
                "title": "Setor 3A"
            },
            {
                "id": "4",
                "tittle": "Setor 3B"
            },
            {
                "id": "5",
                "tittle": "Setor 4C"
            },
            {
                "id": "6",
                "tittle": "Setor 5"
            },
            {
                "id": "7",
                "tittle": "Setor 6"
            }
        ]

        wpp.sendOptionList(option)

    if 'Setor' in optionchoice:
        Setor = optionchoice
        wpp.sendText(f'Beleza {senderName}, agora envie o número da casa:')
    if 1 <= message <= 70:
        Casa = message
        setor_usuario = Setor
        casa_usuario = Casa
        informacoes = api.buscar_informacoes(setor_usuario, casa_usuario)

        if informacoes:
            wpp.sendText("Proprietário:", informacoes["Proprietário"])
            wpp.sendText("Rotas:", informacoes["Rotas"])
        else:
            wpp.sendText("Informações não encontradas para o setor e casa fornecidos.")
    response = data
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=False, host=host)  # Inicia o servidor Flask em modo de depuração