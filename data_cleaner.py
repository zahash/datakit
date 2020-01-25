import pandas as pd
import re


def preprocess(df, column_dtype_conversion_dictionary, std_coeff, fill_na_method):
    '''
    Args:
        column_dtype_conversion_dictionary: dictionary having keys as the 
            column name and value as the desired dtype

        std_coeff: coefficient of standard deviation in outlier removal

        fill_na_method: 'mean' or 'median'. nan values of each column will
            be replaced by that column's mean or median
    '''
    df = sanitize_column_names(df)
    df = change_dtypes(df, column_dtype_conversion_dictionary)
    df = df.drop_duplicates()
    df = remove_outliers(df, std_coeff)
    df = fill_nan(df, fill_na_method)

    return df


def sanitize_column_names(df):
    '''
    changes the column names to lowercase, strips any leading and trailing white space,
    replaces space between words to underscores
    '''

    df.columns = [re.sub(" +", " ", col).strip().lower().replace(" ", "_")
                  for col in df.columns]
    return df


def change_dtypes(df, conversion_dictionary):
    ''' first applies the functions then changes the dtypes '''
    for col_name, dtype in conversion_dictionary.items():
        if dtype in [int, float]:
            df[col_name] = df[col_name].apply(lambda x: dtype(
                ''.join([char for char in x if (char.isdigit() or char == '.')])))

        else:
            df[col_name] = df[col_name].astype({col_name: dtype})

    return df


def remove_outliers(df, std_coeff):
    for col_name in df.columns:
        if df[col_name].dtype in [int, float]:
            df[col_name] = df[col_name].mask(df[col_name].sub(
                df[col_name].mean()).div(df[col_name].std()).abs().gt(std_coeff))

    return df


def fill_nan(df, how):
    for col_name in df.columns:
        if df[col_name].dtype in [int, float]:
            if how == "median":
                df[col_name] = df[col_name].fillna(df[col_name].median())
            elif how == "mean":
                df[col_name] = df[col_name].fillna(df[col_name].mean())
            else:
                raise ValueError("'how' parameter must be 'mean' or 'median'")

    return df
