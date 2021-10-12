import os
import datetime
import pandas as pd
from pandas.core.frame import DataFrame

cwd = os.getcwd()

def main():

  column_file = open(f'{cwd}/data/header.txt', 'r').read()
  columns = column_file.split(',')
  columns = [col.lower() for col in columns]

  parse_dates = ['created date', 'closed date']
  usecols = ['created date', 'closed date', 'incident zip']
  df = pd.read_csv(f"{cwd}/data/nyc_311_limit.csv", names=columns, usecols=usecols, parse_dates=parse_dates)
  df = clean(df)
  calculate_response_times(df)


def data_2020(df: DataFrame) -> DataFrame:
  df_copy: DataFrame = df.copy()

  date_filter = df_copy['closed date'] > pd.to_datetime(datetime.date(year=2020,month=1,day=1))
  df_copy: DataFrame = df_copy[date_filter]

  df_copy.to_csv(f'{cwd}/data/data_trimmed.csv', index=False)

  return df


def clean(df: DataFrame) -> DataFrame:


  df_copy: DataFrame= df.copy()

  # Filter dates to be in 2020
  date_filter = df_copy['closed date'] > pd.to_datetime(datetime.date(year=2020,month=1,day=1))
  df_copy: DataFrame = df_copy[date_filter]

  # Remove invalid close dates and drop date columns
  df.dropna(subset=['closed date'], inplace=True)
  # Remove time from date
  df_copy['closed month'] = pd.to_datetime(df_copy['closed date']).dt.normalize()
  df_copy: DataFrame = df_copy.drop('created date', axis=1)
  df_copy: DataFrame = df_copy.drop('closed date', axis=1)

  # Calculate response times and write to file
  df_copy['response time'] = (df['closed date'] -  df['created date']).astype('timedelta64[h]')
  df_copy.to_csv(f'{cwd}/data/response_times.csv', index=False)

  return df_copy

def calculate_response_times(df: DataFrame) -> None:
  response_by_month: DataFrame = df.drop('incident zip', axis='columns').groupby('closed month').mean()
  response_by_zip: DataFrame = df.groupby(['incident zip', 'closed month' ]).mean()

  response_by_month.to_csv(f"{cwd}/data/response_by_month.csv")
  response_by_zip.to_csv(f"{cwd}/data/response_by_zip.csv")

if __name__ == '__main__':
  main()
