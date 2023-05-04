import pandas as pd


def validate_field_length(data, field_name, required_length):
    if not all(data[field_name].str.len() >= required_length):
        raise ValueError(
            f"No todos los datos en la columna '{field_name}' tienen un minimo de '{required_length}' cracteres")


def validate_there_nan(data, field_name):
    if not all(data[field_name].notna()):
        raise ValueError(f"Hay datos NaN en la columna '{field_name}'")


def validate_min_value(data, field_name, min_value):
    if not all(data[field_name].astype(float) > min_value):
        raise ValueError(
            f"No todos los valores de la columna '{field_name}' son mayores a {min_value}")


def validate_date(data, field_name):
    if not pd.api.types.is_datetime64_any_dtype(data[field_name]):
        raise ValueError(f"Hay registros con fechas no validas")
