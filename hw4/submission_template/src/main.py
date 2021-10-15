import os
import datetime
import pandas as pd
from pandas.core.frame import DataFrame

cwd = os.getcwd()

def main():

  column_file = open('/Users/pyadollahicoveo.com/dev/school/COMP-598/hw4/submission_template/data/header.txt', 'r')
  columns = column_file.read().split(',')
  columns = [col.lower() for col in columns]
  column_file.close()

  parse_dates = ['created date', 'closed date']
  usecols = ['created date', 'closed date', 'incident zip']
  df = pd.read_csv("/Users/pyadollahicoveo.com/dev/school/COMP-598/hw4/submission_template/data/data_trimmed.csv", names=columns, usecols=usecols, parse_dates=parse_dates, low_memory=False)
  df.to_csv('/Users/pyadollahicoveo.com/dev/school/COMP-598/hw4/submission_template/data/data_trimmed_cols.csv')
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
  df_copy.dropna(subset=['incident zip'], inplace=True)
  df_copy['incident zip'] = df_copy['incident zip'].astype(int)
  df_copy['incident zip'] = df_copy['incident zip'].astype(str)

  df_copy.dropna(subset=['closed date'], inplace=True)
  df_copy = df_copy[df_copy['created date'] < df_copy['closed date']]

  df_copy['closed month'] = [x.replace(second=0, minute=0, hour=0, day=1, year=2020) for x in df_copy['closed date']]
  df_copy['closed month'] = df_copy['closed month']
  df_copy['response time'] = (df_copy['closed date'] - df_copy['created date']).astype('timedelta64[h]')





  # date_filter = df_copy['closed date'] > pd.to_datetime(datetime.date(year=2020,month=1,day=1))
  # df_copy: DataFrame = df_copy[date_filter]

  # # Remove invalid close dates and drop date columns
  # df.dropna(subset=['closed date'], inplace=True)
  # # Remove time from date
  # df_copy['closed month'] = pd.to_datetime(df_copy['closed date']).dt.normalize()
  # df_copy: DataFrame = df_copy.drop('created date', axis=1)
  # df_copy: DataFrame = df_copy.drop('closed date', axis=1)

  # # Calculate response times and write to file
  # df_copy['response time'] = (df['closed date'] -  df['created date']).astype('timedelta64[h]')
  # df_copy.to_csv(f'{cwd}/data/response_times.csv', index=False)

  return df_copy

def calculate_response_times(df: DataFrame) -> None:
  response_by_month: DataFrame = df.drop('incident zip', axis=1).groupby('closed month').mean().reset_index()
  response_by_zip: DataFrame = df.groupby(['incident zip', 'closed month' ]).mean().reset_index()

  response_by_month.to_pickle('/Users/pyadollahicoveo.com/dev/school/COMP-598/hw4/submission_template/data/response_times_overall.pkl')
  response_by_zip.to_pickle('/Users/pyadollahicoveo.com/dev/school/COMP-598/hw4/submission_template/data/response_times_by_zip.pkl')

if __name__ == '__main__':
  main()
