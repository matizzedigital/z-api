
import requests
import json

class WhatsAppAPI:
    def __init__(self, phone, instance_id, token_id, client_token) -> None:
        self.phone = phone
        self.token_id = token_id
        self.instance_id = instance_id
        self.client_token = client_token
        self.base_url = f"https://api.z-api.io/instances/{instance_id}/token/{token_id}"

    def sendText(self, message):
        url = f"{self.base_url}/send-text"
        payload = {
            "phone": self.phone,
            "message": message
        }
        headers = {
            'client-token': self.client_token,
            'Content-Type': 'application/json'
        }
        return requests.post(url, data=json.dumps(payload), headers=headers)

    def sendOptionList(self, options):
        url = f"{self.base_url}/send-option-list"
        payload = {
            "phone": self.phone,
            "message": "Selecione a melhor opção:",
            "optionList": {
                "title": "Opções disponíveis",
                "buttonLabel": "Abrir lista de opções",
                "options": options
            }
        }
        headers = {
            'client-token': self.client_token,
            'Content-Type': 'application/json'
        }
        return requests.post(url, data=json.dumps(payload), headers=headers)

    def readMessage(self):
        url = f"{self.base_url}/chats"
        headers = {
            'client-token': self.client_token
        }
        response = requests.get(url, headers=headers)
        return response.text