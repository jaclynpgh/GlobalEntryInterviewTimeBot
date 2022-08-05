#  Adapted from https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/
# https://github.com/guoguo12/global-entry-bot

import requests
import schedule
import time
from datetime import datetime, timedelta
from convertTime import convertTimeToStandard
from twilio.rest import Client
from secret import *


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# imported from a secret.py file locally
def interviewTimes():
    account_sid = ACCOUNT_ID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    APPOINTMENTS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={}&minimum=1"
    LOCATION_IDS = {
        'Pittsburgh': 9200,
        'Nashville': 10260,
        'Philadelphia': 5445,
        'Baltimore': 7940
    }
    print("\nRetrieving Global Entry appointment times...\n")

    for city, id in LOCATION_IDS.items():
        url = APPOINTMENTS_URL.format(id)
        appointments = requests.get(url).json()
        if appointments:
            # formatting to separate date and time
            apptDateTime = str(appointments[0]['startTimestamp'].replace("T", " "))
            timeOnly = apptDateTime.split(' ')[1]
            dateOnly = apptDateTime.split(' ')[0]
            # so you can set to search by city and month
            month = dateOnly.split('-')[1]
            standardTime = convertTimeToStandard(timeOnly)
            notification = "{}: Found an appointment at {}".format(city, dateOnly + " " + standardTime)
            print("{}: Found an appointment at {}".format(city, dateOnly + " " + standardTime))
            # send text message if it matches one of these cities, added conditional to only send text if Nashville has appt. in August
            if city == 'Pittsburgh' or (city == 'Nashville' and month == '08'):
                client.messages \
                    .create(
                    body=notification + ' Schedule your appointment: ' + 'https://ttp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=UP',
                    from_=TWILIO_NUMBER,
                    to=TO_NUMBER
                )
        else:
            print("{}: No appointments available".format(city))


schedule.every(5).seconds.do(interviewTimes)
while 1:
    schedule.run_pending()
    time.sleep(1)
