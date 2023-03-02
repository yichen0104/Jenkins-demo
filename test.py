from jenkins_demo import *

def test_clean_ticker():
  def model_stub(company):
    if company == "Adobe Inc.": return "ADBE"
    if company == "Apple Inc.": return "AAPL"
  df = pd.DataFrame({'Ticker': [np.nan, np.nan, 'ADSK'], 
                    'Name': ['Adobe Inc.', 'Apple Inc.', 'Autodesk'], 
                    'Industry': ['Information Technology	', 'Information Technology', 'Application Software'], 
                    'Sub-Industry': ['Application Software', 'Technology Hardware, Storage & Peripherals	', 'Application Software'],
                    'Headquarters Location': ['San Jose, California', 'San Francisco, California', 'Cupertino, California'],
                    'Date added': ['5/5/1997', '12/1/1989', '11/30/1982'],
                    'Day of week': ['Monday', 'Friday', 'Tuesday']})
  out = clean_ticker(df, model_stub)
  assert(out['Ticker'] == ['ADBE', 'AAPL', 'ADSK']).all()

def test_day_of_week_encoding():
  df = pd.DataFrame({'Ticker': ["ADBE", "AAPL", 'ADSK'], 
                    'Name': ['Adobe Inc.', 'Apple Inc.', 'Autodesk'], 
                    'Industry': ['Information Technology	', 'Information Technology', 'Application Software'], 
                    'Sub-Industry': ['Application Software', 'Technology Hardware, Storage & Peripherals	', 'Application Software'],
                    'Headquarters Location': ['San Jose, California', 'San Francisco, California', 'Cupertino, California'],
                    'Date added': ['5/5/1997', '12/1/1989', '11/30/1982'],
                    'Day of week': ['Monday', 'Friday', 'Tuesday']})
  encoded = day_of_week_encoding(df)
  assert "Day of week" in encoded.columns

test_clean_ticker()
test_day_of_week_encoding()