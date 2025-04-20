import os
import pandas as pd

def load_agg_trade(file_path):
    """
    Loads an aggTrade file into a DataFrame.
    """
    df = pd.read_csv(file_path)
    df['Time'] = df['Time'].str.replace(' IST', '', regex=False)
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S.%f %z', errors='coerce')
    return df

def load_depth20(file_path):
    """
    Loads a depth20 file into a DataFrame.
    """
    df = pd.read_csv(file_path)
    df['Time'] = df['Time'].str.replace(' IST', '', regex=False)
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S.%f %z', errors='coerce')
    return df

def list_files_in_folder(folder_path):
    """
    Returns full paths of all .txt files in a folder.
    """
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
