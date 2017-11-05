# run once a day and email
# hit route to run at once
import requests
import json
from config import settings
from datetime import datetime

from onthisday.resources import email


def onthisday(starting_date='', years_ago=0):
    now_year = datetime.strptime(starting_date, '%Y-%m-%d').year if starting_date else datetime.now().year
    now_month = datetime.strptime(starting_date, '%Y-%m-%d').month if starting_date else datetime.now().month
    now_day = datetime.strptime(starting_date, '%Y-%m-%d').day if starting_date else datetime.now().day
    dates_to_check = []
    if years_ago:
        date = generate_date_with_year(year=now_year - years_ago, month=now_month, day=now_day)
        dates_to_check.append(date)

    else:
        for year in range(settings.START_YEAR_ONTHISDAY, now_year):
            date = generate_date_with_year(year=year - years_ago, month=now_month, day=now_day)
            dates_to_check.append(date)

    results = []
    for date in dates_to_check:
        url = settings.API_BASE_URL + 'cases/?decision_date_min=%s&decision_date_max=%s&format=json' % (date, date)
        matched_cases = json.loads(requests.get(url).content)['results']
        if len(matched_cases):
            for case in matched_cases:
                results.append(case)

    # TODO: convert to friendlier format
    # Should we load casebody as well?
    if len(results):
        email(json.dumps(results))

    return results


def generate_date_with_year(year=2017, month=1, day=1):
    return '%s-%s-%s' % (year, month, day)
