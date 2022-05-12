import requests
from datetime import datetime,timedelta
import pytz

url = "https://api-v2.short.cm/statistics/link/lnk_1xcF_1CQtLm?period=total&tzOffset=0&clicksChartInterval=hour"

headers = {"Accept": "*/*", "Authorization": "sk_mvKjhdOLYM8Wy7P0"}

response = requests.request("GET", url, headers=headers)

r=response.json()
print(r)

#human_clicks = r["humanClicks"]
#tz=r['clickStatistics']['datasets'][0]['data'][0]['x']
#obj = datetime.strptime(tz,"%Y-%m-%dT%H:%M:%S.%fZ")#+timedelta(hours=5,minutes=30)
#asia = pytz.timezone("Asia/Kolkata")
#asia_time=obj.astimezone(asia)
#print(human_clicks)
#print(asia_time)
