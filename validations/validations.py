import pandas as pd


def validate_field_length(data, field_name, required_length):
    if not all(data[field_name].str.len() >= required_length):
        raise ValueError(f"No todos los datos en la columna '{field_name}' tienen un minimo de '{required_length}' cracteres")

# def validate_there_nan(data, field_name):
#     if not all(data[field_name].notna()):
#         raise ValueError(f"Hay datos NaN en la columna '{field_name}'")
# def validate_there_nan(data, field_name):
#     nan_rows = data[data[field_name].isna()].index.tolist()
#     if nan_rows:
#         raise ValueError(f"Hay datos NaN en la(s) fila(s) {nan_rows} de la columna '{field_name}'")

def validate_there_nan(data, field_name):
    nan_rows = data.loc[data[field_name].isna()]
    if not nan_rows.empty:
        index = nan_rows.index[0]  # get the index of the first row
        value = nan_rows[field_name].iloc[0]  # get the value of the field
        raise ValueError(f"Hay un dato NaN en la fila {index} de la columna '{field_name}'. Valor: {value}")


    
def validate_min_value(data, field_name, min_value):
    if not all(data[field_name].astype(float) > min_value):
        raise ValueError(f"No todos los valores de la columna '{field_name}' son mayores a {min_value}")
    
def validate_date(data, field_name):
    if not pd.api.types.is_datetime64_any_dtype(data[field_name]):
        raise ValueError(f"Not all '{field_name}' fields are dates")
        