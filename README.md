# Envio de SMS com Twilio

Este repositório contém um script em Python para enviar mensagens SMS utilizando a biblioteca Twilio. O Twilio é um serviço de comunicação em nuvem que permite enviar e receber mensagens SMS e realizar chamadas telefônicas por meio de uma API fácil de usar.

## Pré-requisitos

Antes de usar o script de envio de SMS, você precisará dos seguintes pré-requisitos:

- Python 3 instalado em seu sistema. Você pode fazer o download e instalá-lo a partir do site oficial do Python (https://www.python.org).

- Conta no Twilio: Para utilizar o Twilio, você precisará criar uma conta. Você pode se inscrever gratuitamente no site do Twilio (https://www.twilio.com) e obter as credenciais necessárias para autenticação.

- Biblioteca Twilio: O script utiliza a biblioteca Twilio para interagir com a API do Twilio. Você pode instalar a biblioteca Twilio usando o gerenciador de pacotes pip, executando o seguinte comando em seu terminal:

```bash
pip install twilio
```
## Configuração
Abra o arquivo `sendsms.py` em um editor de texto de sua escolha.

Localize as seguintes variáveis no código:

- `account_sid`: Substitua pelo SID da sua conta do Twilio. Você pode encontrar o SID da conta no painel de controle do Twilio.

- `auth_token`: Substitua pelo token de autenticação da sua conta do Twilio. Assim como o SID da conta, você pode encontrar o token de autenticação no painel de controle do Twilio.

- `numero_twilio`: Substitua pelo número de telefone fornecido pelo Twilio que será usado como o número remetente.

Salve as alterações no arquivo.

## Uso

Para usar o script de envio de SMS, siga as etapas abaixo:

1. Abra um terminal e navegue até o diretório do projeto.

2. Execute o script com o seguinte comando:

   ```bash
   python sendsms.py

Siga as instruções fornecidas pelo script:

- **Informe o número de destino:** Digite o número de telefone para o qual você deseja enviar a mensagem SMS. Certifique-se de incluir o código do país e o sinal de "+" na frente do número.

- **Escreva a mensagem:** Digite a mensagem que deseja enviar.

- **Confirme o envio:** O script solicitará sua confirmação antes de enviar a mensagem. Digite "Y" para confirmar o envio ou "N" para cancelar.

Após a confirmação, o script utilizará a biblioteca Twilio para enviar a mensagem SMS para o número de destino fornecido.

## Créditos

Este código foi desenvolvido por [Raul Lopes](https://www.linkedin.com/in/eu-raullopes/).

- Instagram: [@eu.raullopes](https://www.instagram.com/eu.raullopes/)
- LinkedIn: [eu-raullopes](https://www.linkedin.com/in/devraullopes/)
- E-mail: raulsilva67@outlook.com.br





