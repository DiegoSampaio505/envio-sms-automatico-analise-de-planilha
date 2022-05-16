import pandas as pd
from twilio.rest import Client


account_sid = "ACa6fc319eb41581b9aa3b42c66fad547d"
auth_token  = "78ebdd5f346cf5c7913dc1b2565eb723"

client = Client(account_sid, auth_token)


lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        message = client.messages.create(
            to="+5513991038343",
            from_="+19705123358",
            body=f"No mês de {mes} a vendedora: {vendedor} bateu a meta de vendas com um total de {vendas} em vendas")
        print(message.sid)