# run once a day and email
# hit route to run at once
import requests
from datetime import datetime

def onthisday(date):
    date = date if date else datetime.now()
    requests.get()
