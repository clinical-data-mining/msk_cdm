import os
import pandas as pd

from dotenv import load_dotenv, find_dotenv, dotenv_values


def read_minio_api_config(fname_env):
        config = dotenv_values(fname_env)
        dict_config = dict(config)
        
        load_dotenv(dict_config['MINIO_ENV'])
 
        ACCESS_KEY = os.getenv('ACCESS_KEY')
        SECRET_KEY = os.getenv('SECRET_KEY')
        
        # Add Minio access and secret key to the configure json
        dict_config['ACCESS_KEY'] = ACCESS_KEY
        dict_config['SECRET_KEY'] = SECRET_KEY
        
        return dict_config
    
def read_db2_api_config(fname_env):
    config = dotenv_values(fname_env)
    dict_config = dict(config)
    
    return dict_config

def save_appended_df(df, filename, pathname=None, sep=','):
    # This function saves the combined dataframe
    print('Saving %s' % filename)
    if pathname is not None:
        pathfilename = os.path.join(pathname, filename)
    else:
        pathfilename = filename
    df.to_csv(pathfilename, sep=sep, index=False)

    print('Saved.')

def mrn_zero_pad(df, col_mrn):
    df[col_mrn] = df[col_mrn].astype(str).str.zfill(8)
    return df

def set_debug_console():
    # Console settings
    desired_width = 320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_rows', 250)
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.expand_frame_repr', False)
    # pd.set_option('display.expand_columnwidth', False)
    
def drop_cols(df, cols):
    # Drops columns if available
    cols_d = [x for x in cols if x in df.columns]
    df = df.drop(columns=cols_d)
    return df

def print_df_without_index(df):
    # Prints dataframe to console without indices. Useful when looking to get a list of patient IDs
    print(df.to_string(index=False))
    
    return None

def convert_to_int(df, list_cols):
    df[list_cols] = df[list_cols].apply(lambda x: x.astype(pd.Int32Dtype()))
    
    return df

def convert_to_age(df_input, list_date_cols, col_date_ref, col_id_input, df_ref=None, col_id_ref=None, drop_dates=True):
    # df_input: dataframe containing columns of dates
    # list_date_cols: list of column names where dates are contained
    # col_date_ref: column name of reference date such as birth date
    # col_id_input: Column containing ID key
    # df_ref: dataframe containing reference date (Optional)
    # col_id_ref: Column containing ID key to join with df_input
    # drop_dates: Indicator for dropping columns containing dates
    
    if df_ref is not None:
        # Merge with reference data
        df_ref = df_ref[[col_id_ref, col_date_ref]].drop_duplicates()
        df_input = df_input.merge(right=df_ref, how='left', left_on=col_id_input, right_on=col_id_ref)
        if col_id_input != col_id_ref:
            df_input = df_input.drop(columns=[col_id_ref])
        
    # Convert list of dates to datetime
    list_dates = list_date_cols + [col_date_ref]
    df_input[list_dates] = df_input[list_dates].apply(lambda x: pd.to_datetime(x))
    
    cols_new = ['AGE_' + x for x in list_date_cols]
        
    # Convert to age
    for i, current_date_col in enumerate(list_date_cols):
        age_col = (df_input[current_date_col] - df_input[col_date_ref]).dt.days
        df_input[cols_new[i]] = age_col
        
    # Print IDs with no reference date
    logic_null = df_input[col_id_input].isnull()
    ids_missing_ref = df_input.loc[logic_null, [col_id_input]]
    
    if logic_null.any():
        fname_ids_errors = 'ids_missing_reference_dates.csv'
        ids_missing_ref.to_csv(fname_ids_errors, index=False)
        
    if drop_dates:
        df_input = df_input.drop(columns=list_dates)
        
    return df_input

def get_binary_att(df, col_att, col_id_change, key):
    df[col_att] = df[col_att] == key
    df_out = (df.groupby([col_id_change])[col_att].sum() > 0).reset_index()
    
    return df_out

def convert_col_to_datetime(df, col):
    df[col] = pd.to_datetime(df[col])

    return df

