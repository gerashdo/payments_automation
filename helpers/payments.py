import pandas as pd


def create_payments_dataframe(payments):
    dataframe = pd.DataFrame([
        (p.client.name, p.amount, p.date.strftime('%d/%m/%Y'), p.provider.name) for p in payments],
        columns=['Cliente', 'Monto', 'Fecha', 'Proveedor']
    )

    return dataframe
