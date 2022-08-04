# Global Entry Interview Time Slot Bot

A Python script that notifies you via text if an available Global Entry interview time slot becomes available on the TTP scheduler. Currently the wait times for many airports are months out. This script checks the TTP scheduler every 5 seconds in the event that someone reschedules or cancels.

*Adapted from  https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/, https://github.com/guoguo12/global-entry-bot, and https://github.com/oliversong/goes-notifier*

## Setup

1. Clone this repo to your local environment.

2. Install dependencies 

```
pip install -r requirements.txt
```
3. Make a free Twilio account to send text messsages -> https://www.twilio.com/try-twilio

4. Create a secret.py file locally with the following variables:
```
ACCOUNT_ID = 'Your Twilio Account ID'
AUTH_TOKEN = 'Your Twilio Auth Token'
TWILIO_NUMBER = 'Phone number from Twilio'
TO_NUMBER =  'Your personal number or whoever you want the text sent to'
```
5. Run get_ttp_appointments.py

## Tips
To customize the script to your needs...
Add more location ids here:
```
 LOCATION_IDS = {
        'Pittsburgh': 9200,
        'Nashville': 10260,
        'Philadelphia': 5445,
        'Baltimore': 7940
    }
 ```
 @Oliver Song has all location IDs listed here -> https://github.com/oliversong/goes-notifier
 
 Line 43 is a conditional for what texts you want sent aand can be adjusted to your needs. For example, if you want the bot to only send you a text when an appointment becomes available in Baltimore in October then you would set city to 'Balitmore' and month to '8'. For texts for all months and cities listed in the location dictionary, then omit this line.
 
     if city == 'Pittsburgh' or (city == 'Nashville' and month == '8'):

