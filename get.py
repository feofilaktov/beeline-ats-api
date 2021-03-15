import pandas as pd
import requests
import json

BeelineToken = '' #Токен из ЛК Билайна
HeaderType = 'X-MPBX-API-AUTH-TOKEN'
response = requests.get('https://cloudpbx.beeline.ru/apis/portal/statistics?page=0&pageSize=10',  headers={HeaderType : BeelineToken})
df = pd.DataFrame.from_dict(response.json())
df['startDate'] = df['startDate'].astype(int)//1000 + 21600
df['startDate'] = pd.to_datetime(df['startDate'], unit='s').astype('datetime64[ns, Europe/Moscow]').dt.tz_convert('UTC')
df.to_excel('./data.xlsx')
print(df)
