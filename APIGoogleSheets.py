from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsAPI:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # Define SCOPES aqui

    def __init__(self, spreadsheet_id, range_name):
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        self.service = self.setup_service()

    def setup_service(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return build('sheets', 'v4', credentials=creds)

    def buscar_informacoes(self, setor, casa):
        result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=self.range_name).execute()
        values = result.get('values', [])
        for item in values:
            if item[0] == setor and item[1] == casa:
                return {"Proprietário": item[2], "Rotas": item[3]}
        return None

def main():
    # Configurações
    SAMPLE_SPREADSHEET_ID = '1oREYpTbM1lfUdv6aHssajVRqfRDZQLi9w7Y9wZgtzJg'
    SAMPLE_RANGE_NAME = 'Dados!A1:D146'
    
    # Cria uma instância da classe GoogleSheetsAPI
    api = GoogleSheetsAPI(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)

    # Exemplo de uso:
    setor_usuario = "Setor 1"
    casa_usuario = "2"
    informacoes = api.buscar_informacoes(setor_usuario, casa_usuario)

    if informacoes:
        print("Proprietário:", informacoes["Proprietário"])
        print("Rotas:", informacoes["Rotas"])
    else:
        print("Informações não encontradas para o setor e casa fornecidos.")

if __name__ == '__main__':
    main()
