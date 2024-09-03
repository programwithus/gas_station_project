import pandas as pd


def get_data(PATH):
    df = pd.read_csv(PATH)
    df.drop(['Unnamed: 0'], inplace=True, axis=1)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year.astype(str)
    df['month'] = df['date'].dt.month.astype(str)
    return df