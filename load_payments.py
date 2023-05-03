import pandas as pd

from config.db import SessionLocal

from models.client import Client
from models.provider import Provider
from models.payment import Payment

from validations.validations import validate_field_length, validate_there_nan, validate_min_value, validate_date


bancomer = './data/Bancomer.xlsx'
santander = './data/Santander.xlsx'
banamex = './data/Banamex.xlsx'

dataBancomer = pd.read_excel(bancomer)
dataSantander = pd.read_excel(santander)
dataBanamex = pd.read_excel(banamex)

allData = dataBancomer
# allData = pd.concat([dataBancomer, dataSantander, dataBanamex])
allData['Monto'] = pd.to_numeric(allData['Monto'], errors='coerce')
allData['Fecha'] = pd.to_datetime(allData['Fecha'], errors='coerce')

# print(allData)

if not all(allData.columns == ['Fecha', 'Cliente', 'Monto', 'Proveedor']):
    raise Exception('Columnas no coinciden')

if not all(allData['Fecha']):
    raise Exception('No todos los registros tienen una fecha')
validate_date(allData, 'Fecha')

if not all(allData['Cliente']):
    raise Exception('No todos los registros tienen un cliente')
validate_field_length(allData, 'Cliente', 10)

if not all(allData['Proveedor']):
    raise Exception('No todos los registros tienen un proveedor')
validate_field_length(allData, 'Proveedor', 5)

if not all(allData['Monto']):
    raise Exception('No todos los registros tienen un monto')
validate_there_nan(allData, 'Monto')
validate_min_value(allData, 'Monto', 0)




session = SessionLocal()

for index, row in allData.iterrows():
    current_client = Client(name=row['Cliente'])
    existing_client = session.query(Client).filter(Client.name == current_client.name).first()
    if existing_client:
        current_client = existing_client
    else:
        session.add(current_client)
        session.commit()

    current_provider = Provider(name=row['Proveedor'])
    existing_provider = session.query(Provider).filter(Provider.name == current_provider.name).first()
    if existing_provider:
        current_provider = existing_provider
    else:
        session.add(current_provider)
        session.commit()
    
    payment = Payment(amount=row['Monto'], date=row['Fecha'], client=current_client, provider=current_provider)
    session.add(payment)
    session.commit()

session.close()

print('Se han cargado los pagos correctamente')