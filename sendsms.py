import os
from twilio.rest import Client

def enviar_sms(msg, destinatario):
    # Substitua as informações abaixo pelas suas credenciais do Twilio
    account_sid = "SEU SID" 
    auth_token = "SEU TOKEN"
    numero_twilio = "SEU NUMBER"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_= numero_twilio,
        to=destinatario
    )

print("|" + "=" * 5 + "[SEND SMS]" + "=" * 5 + "|")

# É OBRIGATORIO POR O + e o codigo do pais. 
numero_destino = input("Informe o número: ")
mensagem = input("Escreva a mensagem: ")
os.system("cls")

confirm_send = input("Confirma o envio?\nY or N: ")
if confirm_send.lower() == "y":
     enviar_sms(mensagem, numero_destino)
     print("Mensagem enviada.")
else:
     print("Mensagem cancelada!")
