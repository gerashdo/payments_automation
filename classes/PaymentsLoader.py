import pandas as pd

from validations.validations import (
    validate_date,
    validate_field_length,
    validate_there_nan,
    validate_min_value
)


class PaymentsLoader:

    def __init__(self):
        self.dataframe = None

    def read_file_to_dataframe(self, filename):
        self.dataframe = pd.read_excel(filename)

    def convert_fields_to_valid_types(self):
        self.convert_monto_to_numeric()
        self.convert_fecha_to_datetime()

    def convert_monto_to_numeric(self):
        self.dataframe['Monto'] = pd.to_numeric(
            self.dataframe['Monto'], errors='coerce')

    def convert_fecha_to_datetime(self):
        self.dataframe['Fecha'] = pd.to_datetime(
            self.dataframe['Fecha'], errors='coerce')

    def validate_data(self):
        if not all(self.dataframe.columns == ['Fecha', 'Cliente', 'Monto', 'Proveedor']):
            raise Exception('Columnas no coinciden')

        if not all(self.dataframe['Fecha']):
            raise Exception('No todos los registros tienen una fecha')

        validate_date(self.dataframe, 'Fecha')

        if not all(self.dataframe['Cliente']):
            raise Exception('No todos los registros tienen un cliente')

        validate_field_length(self.dataframe, 'Cliente', 10)

        if not all(self.dataframe['Proveedor']):
            raise Exception('No todos los registros tienen un proveedor')

        validate_field_length(self.dataframe, 'Proveedor', 5)

        if not all(self.dataframe['Monto']):
            raise Exception('No todos los registros tienen un monto')

        validate_there_nan(self.dataframe, 'Monto')

        validate_min_value(self.dataframe, 'Monto', 0)

    def get_dataframe(self):
        return self.dataframe
