import random,json
from sqlite3.dbapi2 import Timestamp as time
import time, datetime, requests


time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:')
url = 'http://127.0.0.1:5000/temp'

temp = { #dict that show data
    'City': "Bangkok", 
    'Temprature': random.randint(-10, 35), 
    'Pressure': random.randint(500, 2000),
    'Humidity': random.randint(10, 200),
    't': time
}
r = requests.post(url, json=temp) #post dict i url if status 200 then is good
print(r.status_code)
