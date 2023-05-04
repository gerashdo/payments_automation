from classes.PaymentsLoader import PaymentsLoader
from classes.PaymentsLoaderService import PaymentsLoaderService


bancomer = './data/Bancomer.xlsx'
santander = './data/Santander.xlsx'
banamex = './data/Banamex.xlsx'

try:
    payment_loader = PaymentsLoader()
    payment_loader.read_file_to_dataframe(bancomer)
    payment_loader.convert_fields_to_valid_types()

    payment_loader.validate_data()
    data = payment_loader.get_dataframe()

    payment_loader_service = PaymentsLoaderService(data)
    payment_loader_service.save_data()

    print('Se han cargado los pagos correctamente')
except Exception as e:
    print(e)
