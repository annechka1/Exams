"""import requests
import json
response = requests.get(
    'https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2020-12-01&enddate=2020-12-07'
)
sum=0
#count=0
data=json.loads(response.text)
for x in data:
    sum=x["Cur_OfficialRate"]+sum
    #count=count+1
currency=sum/len(data)
print(currency)"""