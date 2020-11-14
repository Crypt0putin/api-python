import requests, os, time, logging
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

r = requests.get(input('Введите полный адрес интернет ресурса для мониторинга доступности: '))

def checker(msg):
    message = client.messages.create(
        body = msg,
        from_='+12283357916',
        to = '+79871758544',
    )
    print('Сообщение о доступности ресурса уже в пути!')

if r.ok == False:
    while True:
        msg = 'Привет! Похоже, что целевой ресурс в настоящее время недоступен.'
        checker(msg)
        time.sleep(60)

else:
    msg = 'Привет! Целевой ресурс в настоящее время работает исправно.'
    checker(msg)