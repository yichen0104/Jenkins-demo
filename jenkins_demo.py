import pandas as pd 
import requests

data = pd.read_csv('sp500-constituents.csv')

#data manipulation
def day_of_week_encoding(data):
  if 'Date added' not in data.columns: raise ValueError("Column 'Date added' missing")
  if data['Date added'].dtype != 'object': raise ValueError("Invalid type for column datetime")
  data['Day of week']= pd.to_datetime(data['Date added']).dt.day_name()
  return data

data = day_of_week_encoding(data)

def get_ticker(company_name):
  url = "https://s.yimg.com/aq/autoc"
  parameters = {'query': company_name, 'lang': 'en-US'}
  response = requests.get(url = url, params = parameters)
  data = response.json()
  ticker = data['ResultSet']['Result'][0]['symbol']
  return ticker

#data cleaning
def clean_ticker(data, model):
  def clean(row):
    if pd.isnull(row['Ticker']):
      row['Ticker'] = model(row['Name'])
    return row
  return data.apply(clean, axis=1)

data = clean_ticker(data, get_ticker)

