import os
import os.path
from classes.PaymentsLoader import PaymentsLoader
from classes.PaymentsLoaderService import PaymentsLoaderService

os.system('clear')

exists_file = False
file_path = ''

print('*' * 80 )
print("""El archivo con la información a ser importada debe encontrarse 
en el directorio "data/" a la altura de este script.""")
print('*' * 80 )
print('')
      
while (not exists_file):
    file_name = input('Escribe el nombre del archivo xlsx sin extensión: ')
    file_path = f"./data/{file_name}.xlsx"
    exists_file = os.path.isfile(file_path)
    if not exists_file:
        print('No se encontró un archivo con ese nombre, vuelve a intentarlo')
        print('')


try:
    payment_loader = PaymentsLoader()
    payment_loader.read_file_to_dataframe(file_path)
    payment_loader.convert_fields_to_valid_types()

    payment_loader.validate_data()
    data = payment_loader.get_dataframe()

    payment_loader_service = PaymentsLoaderService(data)
    payment_loader_service.save_data()

    print('Se han cargado los pagos correctamente')
except Exception as e:
    print(e)
